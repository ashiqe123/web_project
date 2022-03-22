from django.urls import path

from regapp import views

urlpatterns = [
    path('',views.demo,name='demo')
]