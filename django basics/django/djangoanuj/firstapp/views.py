from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello world")

def myfunctionabout(request):
    return HttpResponse("About Response")
def add(request,a,b):
    return HttpResponse(a+b)
def intro(request,name,age):
    mydictionary={
        "name":name,
        "age":age
    }
    return JsonResponse(mydictionary)
def myfirstpage(request):
    return render(request,'index.html')
def mysecondpage(request):
    return render(request,'second.html')
def mythirdpage(request):
    var="hello world"
    greeting="hey how many fruits available"
    fruits=["apple","mango","banana"]
    num1,num2=10,4
    ans=num1>num2
   

    mydictionary={
        "var":var,
        "msg":greeting,
        "myfruits":fruits,
        "num1":num1,
        "num2":num2,
        "ans":ans
    }
    return render(request,'third.html',context=mydictionary)
def myimagepage(request):
    return render(request,'imagepage.html')
def myimagepage2(request):
    return render(request,'imagepage2.html')
def myimagepage3(request):
    return render(request,'imagepage3.html')
def myimagepage4(request):
    return render(request,'imagepage4.html')
def myimagepage5(request,imagemname):
    myimagename=str(imagename);
    myimagename=myimagenname.lower();
    print(myimagename)
    if myimagename=="django":
        var=True
    elif myimagename=="python":
        var=False
    mydictionary={
        "var":var
    }
    return render(request,'imagepage5.html',context=mydictionary)
