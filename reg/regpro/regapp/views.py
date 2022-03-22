from django.shortcuts import render
from .models import spec
# Create your views here.
def demo(request):
    obj=spec.objects.all()
    return render(request,'index.html',{'key':obj})