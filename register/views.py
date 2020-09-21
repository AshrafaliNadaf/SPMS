from django.shortcuts import render

# Create your views here.


# def home_page(request):
#     return render(request, 'homePage.html')


def login(request):
    return render(request, 'LoginPage.html')
