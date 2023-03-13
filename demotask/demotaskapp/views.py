from django.http import HttpResponse
from django.shortcuts import render
from.models import menu
# Create your views here.
def demo(request):
    obj=menu.objects.all()
    return render(request,'index.html',{'result':obj})

def about(request):
    return HttpResponse("about me....")

def index(request):
    return render(request,'index1.html')

def multiply(request):
    n1=int(request.GET['num1'])
    n2=int(request.GET['num2'])
    res=n1*n2
    return render(request,'result.html',{'result':res})
