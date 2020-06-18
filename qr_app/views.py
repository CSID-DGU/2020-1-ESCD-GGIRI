import json
from .models import QrAppVisitorVisitrequest
from .models import QrAppVisitRequestList
from .models import QrAppApartment
from django.shortcuts import render,redirect, get_object_or_404
# from __future__ import unicode_literals
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
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
    return render(request, 'qr_app/resQrDisplay.html')

def resRequestedVisit(request):
    return render(request, 'qr_app/resRequestedVisit.html')

def visAfterLogin(request):
    return render(request, 'qr_app/visAfterLogin.html')

def visitForm(request):
    return render(request, 'qr_app/visitForm.html')

def visPermittedVisit(request):
    return render(request, 'qr_app/visPermittedVisit.html')

def visQrDisplay(request):
    return render(request, 'qr_app/visQrDisplay.html')

def doVisitForm(request):
    if request.method=='POST':
        #id=request.POST['uid']
        name=request.POST['uname']
        building=request.POST['building']
        room=request.POST['room']
        purpose=request.POST['purpose']
        id=request.session['v_id']
        new_visitForm=QrAppVisitorVisitrequest(uid=id,name=name, building_id=building,
                                               room_id=room,visit_purpose=purpose)
        new_visitForm.save()
        #디비에서 해당 동 거주자 찾음
        if QrAppApartment.objects.filter(building_id=building,room_id=room):
            resident_uid=QrAppApartment.objects.get(building_id=building,room_id=room)
            resident_uid=resident_uid.uid
            new_list=QrAppVisitRequestList(resident_uid=resident_uid,visitor_uid=id)
            new_list.save()
    return render(request, 'qr_app/visAfterLogin.html')