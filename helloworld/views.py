from django.shortcuts import render
from django.http import HttpResponse

def helloworld(request):
    return HttpResponse("Hello World From MyApp")

def Demohtml(request):
    return render (request,"Demo.html",{})
def logindemo(request):
    return render (request, "login.html",{})

def verifydata(request):
    uname = request.GET["uname"]
    pwd = request.GET["pwd"]
    if(uname=="gagan" and pwd=="saini"):
        return HttpResponse("Login successful...<h1>Welcome"+uname+"</h1>")
    else:
        return HttpResponse("Login failed")

def demoData(request):
    uname="Gagan"
    return render(request,"Welcome.html",{"username":uname})

def demoData1(request):
    uname="Gagan"
    location="Ghaziabad"
    age=22
    return render (request,"display.html",{"username":uname,"location":location, "age":age})