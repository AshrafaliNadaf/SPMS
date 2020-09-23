from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,reverse
from django.contrib import auth
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


# def home_page(request):
#     return render(request, 'homePage.html')


def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.last_name == "admin":
                auth.login(request, user)
                data1 = User.objects.filter(username=request.user)
                return render(request, 'admin_dashboard.html',{'data1':data1})
            elif user.last_name == "staff":
                auth.login(request, user)
                data1 = User.objects.filter(username=request.user)
                return render(request, 'staff_dashboard.html',{'data1':data1})
            elif user.last_name == "faculty":
                auth.login(request, user)
                data1 = User.objects.filter(username=request.user)
                return render(request, 'faculty_dashboard.html',{'data1':data1})
            else :
                auth.login(request, user)
                data1 = User.objects.filter(username=request.user)
                return render(request, 'student_dashboard.html',{'data1':data1})
        else:
            return HttpResponse( 'usernameError')
    else:
        return render(request, 'LoginPage.html')
