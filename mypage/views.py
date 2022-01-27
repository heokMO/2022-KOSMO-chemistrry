from django.shortcuts import render

# Create your views here.
from mypage.models import post_list, myreply_inpost_list


def myinfo(request):
    return render(request,'mypage/myinfo.html')


def mypost(request):
    mem_seq = 1
    mypage_list = post_list(mem_seq)
    return render(request,'mypage/mypost.html', {'mypage_list': mypage_list})


def myreply(request):
    mem_seq = 1
    mypage_list = myreply_inpost_list(mem_seq)
    return render(request,'mypage/myreply.html', {'mypage_list': mypage_list})
