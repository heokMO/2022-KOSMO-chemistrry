from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home/home.html")

def main_page(request):
    return render(request,'home/main_page.html')
