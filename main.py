import numpy as np
import cv2
from datetime import datetime
import time
import copy

class QueueDetector():

    def onChange(self, val): #callback when the user change the detection threshold
        self.threshold = val

    def __init__(self,threshold=25, doRecord=True, showWindows=True):
        print "::QueueDetector init"
        self.writer = None
        self.font = None
        self.doRecord=doRecord #Either or not record the moving object
        self.show = showWindows #Either or not show the 2 windows
        self.frame = None

        self.capture = cv2.VideoCapture('Videos/simulacion_comedor.mp4')
        res, self.frame = self.capture.read() #Take a frame to init recorder

        self.absdiff_frame = None
        self.previous_frame = None

        self.width = self.frame.shape[1]
        self.height = self.frame.shape[0]
        self.surface = self.width * self.height
        self.currentsurface = 0
        self.avg = 0
        self.currentcontours = None
        self.threshold = threshold
        self.isRecording = False
        self.trigger_time = 0 #Hold timestamp of the last detection
        self.font = cv2.FONT_HERSHEY_SIMPLEX #Creates a font

        if doRecord:
            self.initRecorder()

        if showWindows:
            cv2.namedWindow("Image")
            cv2.createTrackbar("Detection treshold: ", "Image", self.threshold, 100, self.onChange)

    def initRecorder(self): #Create the recorder
        codec = cv2.VideoWriter_fourcc(*'MP4V')
        self.writer=cv2.VideoWriter(datetime.now().strftime("%b-%d_%H_%M_%S")+".mp4",codec,20,(self.width,self.height))

    def run(self):
        started = time.time()
        while True:
            res, currentframe = self.capture.read()
            instant = time.time() #Get timestamp o the frame

            self.processImage(currentframe) #Process the image

            valor = self.somethingHasMoved()
            cv2.drawContours(currentframe, self.currentcontours, -1, (0, 0, 255), 2, -1)
            cv2.putText(currentframe, "Current: " + str(self.avg), (25,100),self.font, 1,(255,255,255),2)

            if not self.isRecording:
                if valor:
                    self.trigger_time = instant #Update the trigger_time
                    if instant > started +10: #Wait 5 second after the webcam start for luminosity adjusting etc..
                        print "::Something is moving (%s)!", (instant)
                        if self.doRecord: #set isRecording=True only if we record a video
                            self.isRecording = True
            else:
                if instant >= self.trigger_time +10: #Record during 10 seconds
                    print "::Stop recording"
                    self.isRecording = False
                else:
                    cv2.putText(currentframe,datetime.now().strftime("%b %d, %H:%M:%S"), (25,30),self.font, 1,(255,255,255),2) #Put date on the frame
                    self.writer.write(currentframe) #Write the frame

            if self.show:
                cv2.imshow("Image", currentframe)

            k=cv2.waitKey(1) % 0x100
            if k==27: # Break if user enters 'Esc'.
                break
            elif k == ord('s'):
                cv2.imwrite('captura.jpg', currentframe)

        self.capture.release()
        if self.writer:
            self.writer.release()

    def processImage(self, curframe):
            curframe = cv2.blur(curframe, (5,5)) #Remove false positives

            if self.absdiff_frame is None: #For the first time put values in difference, temp and moving_average
                self.absdiff_frame = curframe.copy()
                self.previous_frame = curframe.copy()
                #Should convert because after runningavg take 32F pictures
                self.average_frame = np.float32(curframe)
            else:
                cv2.accumulateWeighted(curframe, self.average_frame, 0.05) #Compute the average

            #Convert back to 8U frame
            self.previous_frame = np.uint8(self.average_frame)

            self.absdiff_frame = cv2.absdiff(curframe, self.previous_frame) # moving_average - curframe

            self.gray_frame = cv2.cvtColor(self.absdiff_frame, cv2.COLOR_BGR2GRAY) #Convert to gray otherwise can't do threshold
            _, self.gray_frame = cv2.threshold(self.gray_frame, 50, 255, cv2.THRESH_BINARY)

            self.gray_frame = cv2.dilate(self.gray_frame, None, iterations = 15) #to get object blobs
            self.gray_frame = cv2.erode(self.gray_frame, None, iterations = 10)

    def somethingHasMoved(self):
        # Find contours
        contours, hierarchy = cv2.findContours(self.gray_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        self.currentcontours = contours #Save contours

        self.currentsurface = 0
        for contour in contours: #For all contours compute the area
            self.currentsurface += abs(cv2.contourArea(contour))

        self.avg = (self.currentsurface*100)/self.surface #Calculate the average of contour area on the total size
        if self.avg > self.threshold:
            return True
        else:
            return False

if __name__=="__main__":
    print "Main: Starting analysis..."
    detect = QueueDetector(doRecord=False)
    detect.run()

    #Release everything if job is finished
    cv2.destroyAllWindows()

    print "Main: End"
