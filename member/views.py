from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from member.models import Member


def memIDcheck(request):
    idx = request.GET['id']
    res = Member().idcheck(idx)
    return render(request, 'member/idchk.html', {'res': res[0]})


def member_insert(request):
    mem_info = (request.POST['id'], request.POST['pswd1'], request.POST['nickname'])
    Member().memberInsert(mem_info)
    return render(request, "signup/success.html", {'name': request.POST['name']})


def login(request):
    user_id = request.POST['user_id']
    user_pwd = request.POST['user_pwd']
    univ = Member().get_univ(Member().get_seq(user_id))
    if Member().login(user_id, user_pwd):
        request.session['mem_seq'] = Member().get_seq(user_id)
        request.session['id'] = user_id
        request.session['univ'] = univ
        return redirect('home:home')
    else:
        msg = "아이디 또는 비밀번호가 다릅니다."
        return render(request, 'home/login.html', {'error':msg})
