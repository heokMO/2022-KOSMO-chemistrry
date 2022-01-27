from django.shortcuts import render, redirect


# Create your views here.
from reply.models import Reply


def reply_write(request, post_seq):
    Reply().write_reply(request.POST['reply_comment'], post_seq)
    return redirect('help:showpostdetail', post_seq=post_seq)


def delete_reply(request, reply_seq, post_seq):
    Reply().delete_reply(reply_seq)
    return redirect('help:showpostdetail', post_seq=post_seq)