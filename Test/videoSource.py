#!/usr/bin/python

import numpy as np
import cv2
import time

print "Opening video..."
cap = cv2.VideoCapture('../Videos/simulacion_comedor.mp4')	#instanceo el objeto

while(cap.isOpened()):
    ret, frame = cap.read()

    cv2.imshow('frame', frame)
    pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
    print str(pos_frame)+" frames"

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
