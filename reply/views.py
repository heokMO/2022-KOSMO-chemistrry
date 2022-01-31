from django.shortcuts import render, redirect


# Create your views here.
from post.models import Post
from reply.models import Reply
from post.views import show_post_detail


def reply_write(request, post_seq):
    Reply().write_reply(request.POST['reply_comment'], request.session['mem_seq'], post_seq)
    return redirect(Post().get_url(post_seq), post_seq)


def delete_reply(request, reply_seq, post_seq):
    Reply().delete_reply(reply_seq)
    return redirect(Post().get_url(post_seq), post_seq)
