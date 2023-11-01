from django.contrib import admin
from django.urls import path
from basicConcepts import views

urlpatterns = [
    path('',views.Welcome,name='Welcome'),
    path('user/',views.user,name='user')
]
