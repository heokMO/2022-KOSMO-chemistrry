from django.shortcuts import render


# Create your views here.
from signup.models import Signup


def login(request):
    return render(request, "signup/login.html")


def signup(request):
    return render(request, "signup/signup1.html")


def signup2(request):
    mem_seq = Signup().signup1(request.POST)
    return render(request, "signup/signup2.html", {'univ_list':Signup().get_univ_list(), 'mem_seq': mem_seq})


def last_signup(request, mem_seq):
    user_name = Signup().signup2(mem_seq, request.POST)
    return render(request, "signup/success.html", {'user_name':user_name})


