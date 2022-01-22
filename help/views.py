from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request,'help/list.html')

def write(request):
    return render(request,'help/write.html')