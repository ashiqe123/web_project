from django.urls import path

from credentials import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('log',views.log,name='log'),
    path('logut',views.logut,name='logut'),

]