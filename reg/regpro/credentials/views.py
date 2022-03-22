from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages,auth
from django.shortcuts import redirect
# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages,auth
from django.shortcuts import redirect
# Create your views here.
def log(request):
    if request.method == 'POST':
        user = request.POST['un']
        pas = request.POST['pw']
        usr = auth.authenticate(username=user,password=pas)
        if usr is not None:
            auth.login(request,usr)
            return redirect('/')

        else:
            messages.info(request,"invalid credentials")
            return redirect('log')

    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        em = request.POST['email']
        passw = request.POST['pass1']
        cpassw = request.POST['pass2']
        if passw==cpassw:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user allready exists")
                return redirect('register')
            if User.objects.filter(email=em).exists():
                messages.info(request,'Email already taken')
                return redirect('register')
            else:
                usr=User.objects.create_user(password=passw,username=username,first_name=fn,last_name=ln,email=em)
                usr.save();
                print('user created')
                messages.info(request,'new user created')
                return redirect('log')

        else:
            print("password is wrong")
            messages.info(request,"wrong pass word")
            return redirect('register')




    return render(request,"reg.html")

def logut(request):
    auth.logout(request)

    return redirect('/')