
from django.shortcuts import render, redirect


# Create your views here.
def show_post_list(request):
    delivery_list = [(7, '푸라닭 치킨', '오늘 7시에 푸라닭 시키실 분!!', '22/01/23 19:00:00', 0, 1, 'chichi', '22/01/23 19:00:00', 0), ]
    return render(request,'delivery/showpostlist.html',{'delivery_list':delivery_list})

def show_post_write(request):
    return render(request,'delivery/showpostwrite.html')

def show_post_detail(request):
    post_seq = request.GET['post_seq'];

    post_detail = ('푸라닭 치킨', '오늘 7시에 푸라닭 시키실 분!!', '22/01/23 19:00:00', 0, 1, 2, 'chichi', '22/01/23 19:00:00', '오저치고?', 0)
    reply_detail = [('저는 제너럴이요.','dada','22/01/23 20:21:00,',0),
                    ('저는 고추바바삭이요.','jaejae','22/01/23 20:22:00,',0)]

    return render(request, 'delivery/showpostdetail.html', {'post_detail': post_detail,'post_seq':post_seq,'reply_detail':reply_detail})

def show_post_update(request):
    post_seq = request.GET['post_seq'];

    post_detail = ('화장실 좀 깨끗이 쓰세요', 'chichi', '휴지가 날라다니네요')

    return render(request, 'delivery/showpostupdate.html',{'post_detail': post_detail,'post_seq':post_seq})

def post_update(request):
    update_data = [
        request.POST['post_seq'],
        request.POST['title'],
        request.POST['writer'],
        request.POST['content']
    ]
    return redirect('/delivery/showpostdetail?post_seq={}'.format(request.POST['post_seq']))

def post_delete(request):
    delete_data = request.GET['post_seq']
    return redirect('/delivery/showpostlist')