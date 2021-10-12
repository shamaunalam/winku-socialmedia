from django.shortcuts import render,HttpResponse

# Create your views here.
def Login(request):
    return render(request,'landing.html')

def home(request):
    return render(request,'index-2.html')
