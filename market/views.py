from django.shortcuts import render

# Create your views here.
from market.models import postinsert


def bb_write(request):
    return render(request,"market/write.html")

def used(request):
    return render(request,"market/market.html")

UPLOAD_DIR = '/market/static/images/'
def meminsert(request):
    if 'file1' in request.FILES: #메모리에 file1이 있다면, 업로드가 되었다면
        file = request.FILES['file1']
        file_name = file.name
        fp = open(UPLOAD_DIR+file_name,'wb') # 지정 경로에 파일 이름으로 open하고 타입을 wb로 준다.
        # chunks() : 파일을 1바이트단위로 읽어들이는 함수이다.
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
    else:
        file_name = '-'

    mem_info = (int(request.POST['bb_type']), request.POST['univ'], request.POST['writer_seq'] ,request.POST['title'])

    post_contents = (request.POST['content'], 'sysdate', file_name)

    post_detail = (request.POST['malmuri'],request.POST['price'])

    postinsert(mem_info, post_contents, post_detail)
    return render(request,"market/success.html")

def marketlist(request):
    bb_type = 3
    univ = '서울대학교'
    list = list(bb_type,univ)
    return render(request, "market/list.html",{'list':list})


def list(request):
    return render(request,'market/list.html')

def write(request):
    return render(request,'market/write.html')
