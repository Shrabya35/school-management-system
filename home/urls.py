from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path("", views.index, name='home'),
   path("facility", views.facility, name='facility'),
   path("admission", views.admission, name='admission'),
   path("payment", views.payment, name='payment'),
   path("dashboard", views.dashboard, name='dashboard'),
]