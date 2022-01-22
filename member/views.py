from django.shortcuts import render

# Create your views here.
from member.models import idcheck, memberInsert


def memIDcheck(request):
    idx = request.GET['id']
    res = idcheck(idx)
    return render(request, 'member/idchk.html', {'res': res[0]})


def member_insert(request):
    mem_info = (request.POST['id'], request.POST['pswd1'], request.POST['nickname'])
    memberInsert(mem_info)

    return render(request, "signup/success.html", {'name': request.POST['name']})
