from django.shortcuts import render
from django.http import HttpResponse
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

cap=cv2.VideoCapture(0)

#카메라 띄우는 코드
while True:
    _, frame= cap.read()
    decodedObjects=pyzbar.decode(frame)

    for obj in decodedObjects:
        #print("읽어온 데이터",obj.data.decode('ascii'))
        #화면에 qr코드로 부터 읽어온 내용 출력 코드
        cv2.putText(frame,str(obj.data.decode('ascii')),(100,300),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),2)
    cv2.imshow("Frame",frame)

    key=cv2.waitKey(1)
    if key==27:
        break