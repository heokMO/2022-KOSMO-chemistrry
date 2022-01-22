
from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request,'delivery/list.html')

def write(request):
    return render(request,'delivery/write.html')