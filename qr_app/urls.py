from django.urls import path, include
from . import views
urlpatterns = [
    path('qrDisplay/', views.qrDisplay, name = "qrDisplay"),
    path('resAfterLogin/',views.resAfterLogin, name="resAfterLogin"),
    path('resAfterLogin/resQrDisplay',views.resQrDisplay, name="resQrDisplay"),
    path('resAfterLogin/resRequestedVisit',views.resRequestedVisit,name="resRequestedVisit"),
    path('permitTheRequest/<int:id>', views.permitTheRequest, name="permitTheRequest"),
    path('visAfterLogin/',views.visAfterLogin,name="visAfterLogin"),
    path('visAfterLogin/visitForm',views.visitForm, name="visitForm"),
    path('visAfterLogin/visPermittedVisit',views.visPermittedVisit, name="visPermittedVisit"),
    path('visAfterLogin/visQrDisplay', views.visQrDisplay,name="visQrDisplay"),
    path('visAfterLogin/doVisitForm/',views.doVisitForm, name="doVisitForm"),
    #path(r'^doVisitForm/',views.doVisitForm,name="doVisitForm"),
    path('qrScan/', views.qrScan, name="qrScan"),
    path('vis_qrScan/', views.vis_qrScan, name="vis_qrScan"),
]