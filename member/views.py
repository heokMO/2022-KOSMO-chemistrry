from django.shortcuts import render

# Create your views here.
from member.models import idcheck, member_insert


def memIDcheck(request):
    idx = request.GET['id']
    res = idcheck(idx)
    return render(request, 'member/idchk.html', {'res': res[0]})

def memberInsert(request):
    mem_info = (request.POST['id'], request.POST['pwd'], request.POST['nickname'])
    member_insert(mem_info)

    return render(request,"signup/success.html",{'name':request.POST['name']})