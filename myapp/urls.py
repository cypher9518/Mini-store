from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index,name = "myapp"),
    path("about", views.about,name = "about"),
    path("available", views.available,name = "available"),
    path("contact", views.contact,name = "contact"),
    path("address", views.address,name = "address")



]
