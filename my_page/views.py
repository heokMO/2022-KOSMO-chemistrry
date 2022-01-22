from django.shortcuts import render

# Create your views here.
def myinfo(request):
    return render(request,'my_page/myinfo.html')

def postreply(request):
    return render(request,'my_page/postreply.html')