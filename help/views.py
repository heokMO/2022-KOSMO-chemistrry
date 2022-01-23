from django.shortcuts import render

# Create your views here.
def show_post_list(request):
    return render(request,'help/showpostlist.html')

def show_post_write(request):
    return render(request,'help/showpostwrite.html')