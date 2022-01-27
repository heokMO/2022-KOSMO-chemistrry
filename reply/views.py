from django.shortcuts import render, redirect

# Create your views here.
from reply.models import reply_insert


def reply_insert(request,post_seq):
    mem_seq = '2'
    reply_comment = request.POST['reply']
    info = [post_seq, mem_seq, reply_comment]
    reply_insert(info)
    return redirect('help:showpostdetail', post_seq=post_seq)
