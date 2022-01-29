from django.shortcuts import render, redirect

# Create your views here.
from post.models import Post


def show_post_detail(request, post_seq):
    dynamic_url = '{}:showpostdetail'.format(Post().get_board_type(post_seq))
    return redirect(dynamic_url, post_seq)

