from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.home,name="hm"),
    path('adminlogin/',views.admin,name="adm"),
    path('adminview/',views.adminview,name="admview"),
    path('reg/',views.reg,name="reg1"),
    path('vo/',views.vote,name="vot"),
    path('apt/',views.aptd,name="td"),
    path('apy/',views.apys,name="ys"),
    path('app/',views.appk,name="pk"),
    path('tvo/',views.tevote,name="tvot"),
    path('tt/',views.ttr,name="trs"),
    path('tco/',views.tcon,name="con"),
    path('tbj/',views.tbj,name="bjp"),
    path('res/',views.resu,name="res"),
    path('resa/',views.resap,name="ap"),
    path('rest/',views.reste,name="tel"),
    path('sucr/',views.sucr,name="suss"),
    path('nsucr/',views.nsucr,name="nsuc"),
    path('sucv/',views.sucv,name="scv"),
    path('nsucv/',views.nsucv,name="nscv"),
    path('noreg/',views.noreg,name="noreg"),
]