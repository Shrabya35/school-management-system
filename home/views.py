from unicodedata import name
from django.shortcuts import render
from django.shortcuts import render
from home.models import admission1
from home.models import payment1
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
          address2 = request.POST.get('address2')
          phone2 = request.POST.get('phone2')
          rolln = request.POST.get('rolln')
          cardn = request.POST.get('cardn')
          expm = request.POST.get('expm')
          pay = request.POST.get('pay')
          Payment2 = payment1(y2name=y2name, p2name=p2name, address2=address2, phone2=phone2, rolln=rolln, cardn=cardn, expm=expm, pay=pay)
          Payment2.save()


     return render(request,'payment.html')

def dashboard(request):
     return render(request,'dashboard.html')

def student(request):
     alldata = admission1.objects.all()
     context = {'data': alldata} 
     return render(request,'students.html', context)
