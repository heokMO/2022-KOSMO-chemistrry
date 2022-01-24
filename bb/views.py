from django.core.paginator import Paginator
from django.http import request
from django.shortcuts import render, redirect


# Create your views here.
from django.views.decorators.csrf import csrf_protect

from bb.models import test_insert, test_update, test_list, test_delete, test_detail

def help_bb(request):
    tu = test_list()
    return render(request, "bb/help_bb.html")

def help_write(request):
    return render(request,"bb/help_write.html")

def notice_bb(request):
    return render(request, "bb/notice_bb.html") # 이게 forword라 딕셔너리가된대

def notice_write(request):
    return render(request,"bb/notice_write.html")

def help_list(request):
#     # 기존코드
#     # print('method {}'.format(request.method))
#     # items = Address.objects.order_by('idx')
#     address_count = Address.objects.all().count()
#     # print('items =>' ,items)
#     # print(type(items))
#     # print('address_count =>' ,address_count)
#     # print(type(address_count))
#     #페이징 하려고 다시한 코드
#     items = Address.objects.order_by('-idx')
#     # page 값의 초가깂이 1, 아니면 get방식으로 받는 페이지 값 Get.get 이런함수가 잇네?
#     page = int(request.GET.get('page', '1'))
#     # 전체 데이터에서 10줄씩 분할
#     paginator = Paginator(items,'10')
#     addr_list = paginator.get_page(page)
    return render(request, "bb/help_bb.html")  #이게 forword라 딕셔너리가된대


# ======================================================
# def meminsert(request):
#     addr = (request.POST['id'], request.POST['pwd'],
#             request.POST['name'], request.POST['email'],
#             request.POST['tel'], request.POST['addr'])
#     memberinsert(addr)
#     return render(request,"member/success.html",{'name':request.POST['name'],'tel':request.POST['tel'],'pwd':request.POST['pwd']})