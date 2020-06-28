import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import json
#from .models import QrAppResident

def scan(users):
    print(users[0].hash)
    # cap = cv2.VideoCapture(0)
    # font = cv2.FONT_HERSHEY_PLAIN

    # while True:
    #     _, frame = cap.read()

    #     decodedObjects = pyzbar.decode(frame)
    #     for obj in decodedObjects:
    #         #print("Data", obj.data)
            
    #         print((obj.data).decode('ascii'))
    #         #print(hash)
    #         getInfo=(obj.data).decode('ascii')

    #         for user in users:
    #             uid = user.uid
    #             hash = uid + user.hash
    #             print(hash)

    #             if (hash == (obj.data).decode('ascii')):
    #                 temp='authenticated'
    #                 break
    #                 #cv2.putText(frame, hash, (50, 50), font, 2, (255, 0, 0), 3)

    #                 #cv2.putText(frame, "Authenticated", (50, 50), font, 2, (255, 0, 0), 3)
    #             elif (hash!=(obj.data).decode('ascii')):
    #                 temp='unauthenticated'
    #                 #cv2.putText(frame, hash, (50, 50), font, 2, (255, 0, 0), 3)

    #         cv2.putText(frame, temp, (50, 50), font, 2, (255, 0, 0), 3)


    #                 #cv2.putText(frame, "unAuthenticated", (50, 50), font, 2, (255, 0, 0), 3)

    #         """if (obj.data).decode('ascii') == hash:
    #             cv2.putText(frame, "Authenticated", (50, 50), font, 2, (255, 0, 0), 3)
    #         else:
    #             cv2.putText(frame,"Unauthenticated",(50, 50), font, 2, (255, 0, 0), 3)
    #             # print((obj.data).decode('ascii'))"""
    #     cv2.imshow("Frame", frame)


    #     #읽어온 값 frame에서 사용자의 id와 해쉬값을 분리해야 한다
    #     #먼저 거주가 id받아옴
    #     """r_id=request.session['r_id']
    #     r_id_len=len(r_id) #아이디 길이
    #     if r_id in frame:
    #         hash_start_idx=frame.find(r_id)+r_id_len
    #         hash=frame[hash_start_idx:] #여기서 hash는 읽어온 해쉬값
    #         #디비에서 hash값 비교
    #         #같으면 문열림 출력
    #         if((QrAppResident.objects.get(uid=r_id)).hash == hash):
    #             cv2.imshow("Frame",'door is opened')
    #         #안같으면 문안열림
    #         else:
    #             cv2.imshow("Frame",'door is not opened')"""

    #     key = cv2.waitKey(1)


    #     if key == 27:
    #         break

