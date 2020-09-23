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
                return HttpResponse( 'Logged in ADMIN')
            elif user.last_name == "staff":
                auth.login(request, user)
                return HttpResponse( 'Logged in STAFF')
            elif user.last_name == "faculty":
                auth.login(request, user)
                return HttpResponse( 'Logged in FACULTY')
            else :
                auth.login(request, user)
                return HttpResponse( 'Logged in STUDENT')
        else:
            return HttpResponse( 'usernameError')
    else:
        return render(request, 'LoginPage.html')
