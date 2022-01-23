from django.shortcuts import render, redirect


# Create your views here.
def show_post_list(request):
    notice_list = [(3,'화장실 좀 깨끗이 쓰세요','chichi','22/01/23 16:57:00',0,0),
                   (4,'건물외벽 결함으로 인한 안전','chichi','22/01/23 16:58:00',0,0),
                   (5,'건askdj','chichi','22/01/23 16:59:00',0,0)]
    return render(request,'notice/showpostlist.html',{'notice_list':notice_list})

def show_post_write(request):
    return render(request,'notice/showpostwrite.html')

def show_post_detail(request):
    post_seq = request.GET['post_seq'];

    post_detail = ('화장실 좀 깨끗이 쓰세요','chichi','휴지가 날라다니네요',0,'22/01/23 16:57:00',2)
    reply_detail = [('알겠습니다.','dada','22/01/23 20:21:00,',0),
                    ('저는 아닙니다.','jaejae','22/01/23 20:22:00,',0)]

    return render(request, 'notice/showpostdetail.html', {'post_detail': post_detail,'post_seq':post_seq,'reply_detail':reply_detail})

def show_post_update(request):
    post_seq = request.GET['post_seq'];

    post_detail = ('화장실 좀 깨끗이 쓰세요', 'chichi', '휴지가 날라다니네요')

    return render(request, 'notice/showpostupdate.html',{'post_detail': post_detail,'post_seq':post_seq})

def post_update(request):
    update_data = [
        request.POST['post_seq'],
        request.POST['title'],
        request.POST['writer'],
        request.POST['content']
    ]

    return redirect('/notice/showpostdetail?post_seq={}'.format(request.POST['post_seq']))


def post_delete(request):
    delete_data = request.GET['post_seq']
    return redirect('/notice/showpostlist')


