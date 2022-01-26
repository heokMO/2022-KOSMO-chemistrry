from django.shortcuts import render, redirect

# Create your views here.
from help.models import help_list, help_insert, help_detail, help_update, help_delete, show_post_modify


def show_post_list(request):
    post_list = help_list()
    return render(request,'help/showpostlist.html',{'post_list':post_list})


def show_post_write(request):
    return render(request,'help/showpostwrite.html')


def post_insert(request):
    univ = '국민대학교'
    title = request.POST['title']
    mem_seq = '2'
    content = request.POST['content']

    help_insert(univ=univ, title=title, mem_seq=mem_seq, content=content)
    return redirect('/help/showpostlist')


def show_post_detail(request,post_seq):
    post_detail = help_detail(post_seq)
    reply_detail = [('알겠습니다.', 'dada', '22/01/23 20:21:00,', 0),
                    ('저는 아닙니다.', 'jaejae', '22/01/23 20:22:00,', 0)]
    return render(request,'help/showpostdetail.html',{'post_detail':post_detail,'post_seq':post_seq,'reply_detail':reply_detail})


def show_post_update(request,post_seq):
    post_seq = post_seq
    post_detail = show_post_modify(post_seq)
    return render(request, 'help/showpostupdate.html', {'post_detail': post_detail, 'post_seq': post_seq})


def post_update(request,post_seq):
    info = [request.POST.get('title'),request.POST.get('content'),post_seq]
    help_update(info)
    return redirect('help:showpostdetail', post_seq=post_seq)


def post_delete(request,post_seq):
    help_delete(post_seq)
    return redirect('help:showpostlist')












