from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, "mypage/login.html")


def mainpage(request):
    return render(request, "mypage/mainpage.html")


def memberjoin(request):
    return render(request, "mypage/memberjoin.html")
