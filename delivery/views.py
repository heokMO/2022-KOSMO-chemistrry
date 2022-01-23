
from django.shortcuts import render

# Create your views here.
def show_post_list(request):
    return render(request,'delivery/showpostlist.html')

def show_post_write(request):
    return render(request,'delivery/showpostwrite.html')