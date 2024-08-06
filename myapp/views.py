from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from myown import settings
from .models import Reg,Apreg,Tsreg,Pollsap,Pollsts
from django.core.mail import send_mail
# Create your views here.

def home(request):
    return render(request,'ht/index.html')

def admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username=="admin" and password=="admin123":
            return render(request,"ht/adminview.html")
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request,'ht/admin.html')

def adminview(request):
    return render(request,'ht/adminview.html')

def reg(request):
   try:
            if request.method=="POST":
                n=request.POST['na']
                d=request.POST['do']
                e=request.POST['ms']
                sa=request.POST['st']
                a=request.POST['an']
                s='Andhra Pradesh'
                t=settings.EMAIL_HOST_USER
                sbj='Successfully Registered'
                m=f"Hello {n} \nThank You \n Successfully Registered For Online Voting \n Please Go and Vote For your state Your Vote is valuable to us"
                if(s==sa):
                      x=Reg.objects.create(name=n,dob=d,em=e,sap=sa,ste='no',ad=a)
                      K=Apreg.objects.create(ad=a,sap=sa)
                      b=send_mail(sbj,m,t,[e])
                      return redirect('/sucr')
                else:
                    z=Reg.objects.create(name=n,dob=d,em=e,sap='no',ste=sa,ad=a)
                    n=Tsreg.objects.create(ad=a,ste=sa)
                    b=send_mail(sbj,m,t,[e])
                    return redirect('/sucr')
   except:
      return redirect('/nsucr')
       
   return render(request,'ht/reg.html')

def vote(request):
    return render(request,'ht/vote.html')

def aptd(request):
    try:
       if request.method=="POST":
        a=request.POST['an']
        x=Apreg.objects.filter(ad=a).count()
        if(x>0):
            n=Pollsap.objects.create(ad=a,td=1,ys=0,no=0)
            return redirect('/sucv')
        else:
            return redirect('/noreg')
    except:
        return redirect('/nsucv')

    return render(request,'ht/polla.html')

def apys(request):
    try:
       if request.method=="POST":
        a=request.POST['an']
        x=Apreg.objects.filter(ad=a).count()
        if(x>0):
            n=Pollsap.objects.create(ad=a,td=0,ys=1,no=0)
            return redirect('/sucv')
        else:
            return redirect('/noreg')
    except:
        return redirect('/nsucv')
    
    return render(request,'ht/pollb.html')

def appk(request):
    try:
       if request.method=="POST":
        a=request.POST['an']
        x=Apreg.objects.filter(ad=a).count()
        if(x>0):
            n=Pollsap.objects.create(ad=a,td=0,ys=0,no=1)
            return redirect('/sucv')
        else:
            return redirect('/noreg')
    except:
        return redirect('/nsucv')
    
    return render(request,'ht/pollc.html')

def tevote(request):
    return render(request,'ht/tvote.html')

def ttr(request):
    try:
       if request.method=="POST":
        a=request.POST['an']
        x=Tsreg.objects.filter(ad=a).count()
        if(x>0):
            n=Pollsts.objects.create(ad=a,tr=1,co=0,bj=0)
            return redirect('/sucv')
        else:
            return redirect('/noreg')
    except:
        return redirect('/nsucv')
    
    return render(request,'ht/tpollr.html')

def tcon(request):
    try:
       if request.method=="POST":
        a=request.POST['an']
        x=Tsreg.objects.filter(ad=a).count()
        if(x>0):
            n=Pollsts.objects.create(ad=a,tr=0,co=1,bj=0)
            return redirect('/sucv')
        else:
            return redirect('/noreg')
    except:
        return redirect('/nsucv')
    
    return render(request,'ht/tpollc.html')

def tbj(request):
    try:
       if request.method=="POST":
        a=request.POST['an']
        x=Tsreg.objects.filter(ad=a).count()
        if(x>0):
            n=Pollsts.objects.create(ad=a,tr=0,co=0,bj=1)
            return redirect('/sucv')
        else:
            return redirect('/noreg')
    except:
        return redirect('/nsucv')
    
    return render(request,'ht/tpollb.html')

def resu(request):
    return render(request,'ht/res.html')

def resap(request):
    t=Pollsap.objects.filter(td=1).count()
    y=Pollsap.objects.filter(ys=1).count()
    p=Pollsap.objects.filter(no=1).count()
    z=t+y+p
    if(t>y and t>p):
        b=f"TDP PARTY WINS IN THE ELECTION WITH {t}"
    elif(y>t and y>p):
        b=f"YSRCP PARTY WINS IN THE ELECTION WITH {y}"
    else:
        b=f"JANASEENA PARTY WINS IN THE ELECTION WITH {p}"
    return render(request,'ht/resa.html',{'t':z,'td':t,'ys':y,'pk':p,'re':b}) 

def reste(request):
    t=Pollsts.objects.filter(tr=1).count()
    y=Pollsts.objects.filter(co=1).count()
    p=Pollsts.objects.filter(bj=1).count()
    z=t+y+p
    if(t>y and t>p):
        b=f"TRS PARTY WINS IN THE ELECTION WITH {t}"
    elif(y>t and y>p):
        b=f"CONGRESS PARTY WINS IN THE ELECTION WITH {y}"
    else:
        b=f"BJP PARTY WINS IN THE ELECTION WITH {p}"
    return render(request,'ht/rest.html',{'t':z,'tr':t,'co':y,'bj':p,'re':b})

def sucr(request):
    return render(request,'ht/rsuc.html')

def nsucr(request):
    return render(request,'ht/nsuc.html')

def sucv(request):
    return render(request,'ht/sucv.html')

def nsucv(request):
    return render(request,'ht/nsucv.html')

def noreg(request):
    return render(request,'ht/noreg.html')






