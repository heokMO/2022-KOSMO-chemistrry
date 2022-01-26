from django.shortcuts import render, redirect


def show_post_list(request):
    post_list = [(6, '신입생입니다','시간표는 어떻게 짜는건가요?','22/01/24 14:24:00','chichi',3,1),
                 (7,'헬스다녀보려고 하는데','pt 필수결제해야해?','22/01/24 14:35:00','dada',2,1)]

    return render(request, 'help/showpostlist.html', {'post_list': post_list})


def show_post_write(request):
    return render(request, 'help/showpostwrite.html')


def show_post_detail(request, post_seq):
    post_detail = ['신입생입니다', 'chichi', '22/01/24 14:24:00','시간표는 어떻게 짜는건가요?',3,1]
    reply_detail = [('알겠습니다.', 'dada', '22/01/23 20:21:00,', 0),
                    ('저는 아닙니다.', 'jaejae', '22/01/23 20:22:00,', 0)]

    return render(request, 'help/showpostdetail.html', {'post_detail': post_detail, 'post_seq': post_seq, 'reply_detail': reply_detail})


def show_post_update(request, post_seq):
    post_detail = ['신입생입니다', 'chichi', '시간표는 어떻게 짜는건가요?']
    return render(request, 'help/showpostupdate.html', {'post_detail': post_detail, 'post_seq': post_seq})


def post_update(request, post_seq):
    return redirect('/help/showpostdetail?post_seq={}'.format(post_seq))


def post_delete(request, post_seq):
    return redirect('/help/showpostlist')
