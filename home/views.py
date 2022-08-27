from unicodedata import name
from django.shortcuts import render
from django.shortcuts import render
from home.models import admission
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
          Admission = admission(yname=yname, pname=pname, occupation=occupation, phone=phone,dob=dob, address=address, email=email)
          Admission.save()


     return render(request,'admission.html')

def payment(request):
     return render(request,'payment.html')

def dashboard(request):
     return render(request,'dashboard.html')