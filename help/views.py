from django.shortcuts import render, redirect

from help.models import Help
from reply.models import Reply


def show_post_write(request):
    return render(request, 'help/showpostwrite.html')


def post_write(request):
    Help().post_insert(request.session['mem_seq'], request.POST)
    return redirect('help:showpostlist')


def show_post_list(request):
    post_list = Help().post_list(request.session['mem_seq'])
    return render(request, 'help/showpostlist.html', {'post_list': post_list})


def show_post_detail(request, post_seq):
    post_info = Help().post_detail(post_seq)
    reply_detail = Reply().show_reply_list(post_seq)
    return render(request, 'help/showpostdetail.html', {'post_seq': post_seq, 'post_detail': post_info, 'reply_detail': reply_detail})


def show_post_update(request, post_seq):
    post_detail = Help().post_update_detail(post_seq)
    return render(request, 'help/showpostupdate.html', {'post_detail': post_detail, 'post_seq': post_seq})


def post_update(request, post_seq):
    Help().post_update(post_seq, request.POST)
    return redirect('help:showpostdetail', post_seq=post_seq)


def post_delete(request, post_seq):
    Help().post_delete(post_seq)
    return redirect('help:showpostlist')
