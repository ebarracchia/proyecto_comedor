#!/usr/bin/python

import cv2.cv as cv
import time

cv.NamedWindow("camera", cv.CV_WINDOW_NORMAL)	#Abre una ventana para visualizar imagenes (nombre,parametro)

capture = cv.CaptureFromCAM(0)	#instanceo el objeto

while True:
    img = cv.QueryFrame(capture)
    cv.ShowImage("camera", img)
    if cv.WaitKey(10) == 27:
        break
cv.DestroyAllWindows()	#destruye todas las ventanas creadas con NamedWindow s
