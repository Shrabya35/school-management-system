from unicodedata import name
from django.shortcuts import render
from django.shortcuts import render
from home.models import admission1
from home.models import payment1
from home.models import admin1
# Create your views here.
def index(request):
     return render(request,'index.html')

def facility(request):
     return render(request,'facility.html')

def admission(request):
     if request.method == "POST":
          yname = request.POST.get('yname')
          pname = request.POST.get('pname')
          occupation = request.POST.get('occupation')
          phone = request.POST.get('phone')
          dob = request.POST.get('dob')
          address = request.POST.get('address')
          email = request.POST.get('email')
          Admission2 = admission1(yname=yname, pname=pname, occupation=occupation, phone=phone,dob=dob, address=address, email=email)
          Admission2.save()


     return render(request,'admission.html')

def payment(request):
     if request.method == "POST":
          y2name = request.POST.get('y2name')
          p2name = request.POST.get('p2name')
          email2 = request.POST.get('email2')
          phone3 = request.POST.get('phone3')
          cardn = request.POST.get('cardn')
          expm = request.POST.get('expm')
          pay = request.POST.get('pay')
          Payment2 = payment1(y2name=y2name, p2name=p2name, email2=email2, phone3=phone3, cardn=cardn, expm=expm, pay=pay)
          Payment2.save()


     return render(request,'payment.html')

def dashboard(request):
     return render(request,'dashboard.html')

def student(request):
     alldata = admission1.objects.all()
     context = {'data': alldata} 
     return render(request,'students.html', context)

def admin2(request):
     class_id = request.POST.get('class_id')
     passw = request.POST.get('passw')
     time = request.POST.get('time')
     grade = request.POST.get('grade')
     link = request.POST.get('link')
     Teacher = admin1(class_id=class_id, passw=passw, time=time, grade=grade, link=link)
     Teacher.save()

def class1(request):
     allclass = admin1.objects.all()
     context1 = {'class2': allclass} 
     return render(request,'class.html', context1)