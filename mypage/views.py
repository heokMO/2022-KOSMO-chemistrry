from django.shortcuts import render, redirect

# Create your views here.
from mypage.models import show_myinfo, info_modify


def my_info(request):
    mem_seq = 2
    user_info = show_myinfo(mem_seq)
    return render(request, 'mypage/myinfo.html', {'myinfo': user_info})


def info_update(request):
    mem_seq = 2
    info = request.POST
    info_modify(mem_seq, info)
    return redirect('mypage:myinfo')

def mypost(request):
    mem_seq = 1
    mypage_list = post_list(mem_seq)
    return render(request,'mypage/mypost.html', {'mypage_list': mypage_list})


def myreply(request):
    mem_seq = 1
    mypage_list = myreply_inpost_list(mem_seq)
    return render(request,'mypage/myreply.html', {'mypage_list': mypage_list})
