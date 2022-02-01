from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, "home/login.html")

def logout(request):
    del request.session['mem_seq']
    return render(request, "home/login.html")


def home(request):
    return render(request, 'home/home.html')
