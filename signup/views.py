from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, "signup/login.html")


def mainpage(request):
    return render(request, "signup/mainpage.html")


def memberjoin(request):
    return render(request, "signup/signup.html")
