from django.shortcuts import render, redirect

# Create your views here.
from mypage.models import Mypage


def my_info(request):
    mem_seq = request.session['mem_seq']
    user_info = Mypage().show_myinfo(mem_seq)
    return render(request, 'mypage/myinfo.html', {'myinfo': user_info})


def info_update(request):
    mem_seq = request.session['mem_seq']
    info = request.POST
    Mypage().info_modify(mem_seq, info)
    return redirect('mypage:myinfo')


def my_post(request):
    mem_seq = request.session['mem_seq']
    mypage_list = Mypage().post_list(mem_seq)
    return render(request, 'mypage/mypost.html', {'mypage_list': mypage_list})


def my_reply(request):
    mem_seq = request.session['mem_seq']
    mypage_list = Mypage().myreply_inpost_list(mem_seq)
    return render(request, 'mypage/myreply.html', {'mypage_list': mypage_list})

