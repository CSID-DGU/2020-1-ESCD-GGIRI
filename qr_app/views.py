import json
from .models import QrAppVisitorVisitrequest
from .models import QrAppVisitRequestList
from .models import QrAppApartment
from .models import QrAppDevice
from .models import QrAppResident
from .models import QrAppVisitor
from django.shortcuts import render,redirect, get_object_or_404
# from __future__ import unicode_literals
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from random import *
import pdb
from .qrScan import scan
# import qrcode
# import cv2

# def my_view(request):

#     # Let's assume that the visitor uses an iPhone...
#     request.user_agent.is_mobile # returns True
#     request.user_agent.is_tablet # returns False
#     request.user_agent.is_touch_capable # returns True -> 이거3개 이넘
#     request.user_agent.is_pc # returns False
#     request.user_agent.is_bot # returns False

#     # Accessing user agent's browser attributes
#     request.user_agent.browser  # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
#     request.user_agent.browser.family  # returns 'Mobile Safari'
#     request.user_agent.browser.version  # returns (5, 1)
#     request.user_agent.browser.version_string   # returns '5.1'

#     # Operating System properties
#     request.user_agent.os  # returns OperatingSystem(family=u'iOS', version=(5, 1), version_string='5.1')
#     request.user_agent.os.family  # returns 'iOS' ->이거
#     request.user_agent.os.version  # returns (5, 1)->이거
#     request.user_agent.os.version_string  # returns '5.1' -> 이거

#     # Device properties
#     request.user_agent.device  # returns Device(family='iPhone')
#     request.user_agent.device.family  # returns 'iPhone'

def createQR(request):
    #faqs = Faq.objects.all()
    #context={'faqs':faqs}
    img = qrcode.make("Hello World!")
    img.save("qrCreate_app/static/qrCreate_app/images/helloworld_qrcode.png")
    return render(request,'./qr.html',)


def qrDisplay(request):
    qrCode="Os info"
    return render(request, 'qr_app/qrDisplay.html',{'qrCode':qrCode})

def resAfterLogin(request):
    return render(request, 'qr_app/resAfterLogin.html')

def resQrDisplay(request):
    user_id = (QrAppResident.objects.get(uid=request.session['r_id'])).uid
    rand_salt = randrange(1000000)
    #여기서 새로운 salt가지고 해쉬값 저장
    hash='aaa'
    #DB에 새로운 salt값 hash값 저장 #DB수정부분
    ##resident=QrAppResident(uid=user_id)
    #resident.salt=rand_salt
    #resident.hash=hash

    #사용자로부터 받아온 os정보 같은지 확인(일단 같은지만 확인)
    #사용자로부터 디바이스 정보 받아옴
    os_family = request.user_agent.os.family
    os_version = request.user_agent.os.version_string
    if request.user_agent.is_mobile:
        device_type = 'mobile'
    elif request.user_agent.is_tablet:  # returns False
        device_type = 'tablet'  # returns True -> 이거3개 이넘
    elif request.user_agent.is_pc:  # returns False
        device_type = 'pc'
    #디비에 존재하는 정보와 비교
    if QrAppDevice(uid=user_id, device_type=device_type,os=os_family, version=os_version):
        #사용자 residentDB로 부터 hash값 받아오고 거기에 userid붙여서 qrCode에 저장
        hash = QrAppResident.objects.get(uid=request.session['r_id']).hash
        qrCode=user_id+hash
    return render(request, 'qr_app/resQrDisplay.html',{'qrCode':qrCode})  

# 방문요청 허가 -> 방문요청 리스트 띄우기
def resRequestedVisit(request):
    user_id = (QrAppResident.objects.get(uid=request.session['r_id'])).uid
    apartment = QrAppApartment.objects.get(uid = user_id)
    requestList = QrAppVisitorVisitrequest.objects.filter(building_id = apartment.building_id, floor = apartment.floor_id, room_id = apartment.room_id)
    return render(request, 'qr_app/resRequestedVisit.html', {'requestList': requestList})

def visAfterLogin(request):
    return render(request, 'qr_app/visAfterLogin.html')

def visitForm(request):
    return render(request, 'qr_app/visitForm.html')

# 방문자 -> 허가된 방문요청 리스트 띄우기
def visPermittedVisit(request):
    id=request.session['v_id']
    permitted_request_list = QrAppVisitorVisitrequest.objects.filter(uid = id, permit = 1)
    return render(request, 'qr_app/visPermittedVisit.html', {'permitted_request_list': permitted_request_list})


def visQrDisplay(request):
    user_id = (QrAppVisitor.objects.get(uid=request.session['v_id'])).uid
    hash = QrAppVisitor.objects.get(uid=request.session['v_id']).hash

    qrCode = user_id + hash
    return render(request, 'qr_app/visQrDisplay.html', {'qrCode': qrCode})

def doVisitForm(request):
    if request.method=='POST':
        #id=request.POST['uid']
        name=request.POST['uname']
        building=request.POST['building']
        floor=request.POST['floor']
        room=request.POST['room']
        purpose=request.POST['purpose']
        id=request.session['v_id']
        new_visitForm=QrAppVisitorVisitrequest(uid=id,name=name, building_id=building, floor = floor,
                                               room_id=room,visit_purpose=purpose)
        new_visitForm.save()
        #디비에서 해당 동 거주자 찾음
        if QrAppApartment.objects.filter(building_id=building,room_id=room):
            resident_uid=QrAppApartment.objects.get(building_id=building,room_id=room)
            resident_uid=resident_uid.uid
            new_list=QrAppVisitRequestList(resident_uid=resident_uid,visitor_uid=id)
            new_list.save()
    return render(request, 'qr_app/visAfterLogin.html')


def permitTheRequest(request, id):
    theRequest = QrAppVisitorVisitrequest.objects.get(idx = id)
    theRequest.permit = 1
    theRequest.save()
    return render(request, 'qr_app/resAfterLogin.html')


def qrScan(request):
    #uid = request.session['r_id']
    #resident = QrAppResident.objects.get(uid=uid)
    #hash = uid + resident.hash
    users = QrAppResident.objects.all()
    # print(users)
    scan(users)
    #print(a.all)
    return render(request,'qr_app/qrScan.html')


def vis_qrScan(request):
    users = QrAppVisitor.objects.all()
    scan(users)




    