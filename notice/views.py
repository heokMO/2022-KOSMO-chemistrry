from typing import Dict, Any

from django.shortcuts import render, redirect

from notice.models import Notice
from reply.models import Reply


def show_post_write(request):
    return render(request, 'notice/showpostwrite.html')


def post_write(request):
    Notice().post_insert(request.POST)
    return redirect('notice:showpostlist')


def show_post_list(request):
    notice_list = Notice().post_list()
    return render(request, 'notice/showpostlist.html', {'notice_list': notice_list})


def show_post_detail(request, post_seq):
    post_info = Notice().post_detail(post_seq)
    reply_detail = Reply().show_reply_list(post_seq)
    return render(request, 'notice/showpostdetail.html', {'post_seq': post_seq, 'post_detail': post_info, 'reply_detail': reply_detail})


def show_post_update(request, post_seq):
    post_info = Notice().post_update_detail(post_seq)
    return render(request, 'notice/showpostupdate.html', {'post_detail': post_info, 'post_seq': post_seq})


def post_update(request, post_seq):
    Notice().post_update(post_seq, request.POST)
    return redirect('notice:showpostdetail', post_seq=post_seq)


def post_delete(request, post_seq):
    Notice().post_delete(post_seq)
    return redirect('notice:showpostlist')



