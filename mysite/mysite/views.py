from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    text = request.GET.get('text','default')
    capitalize = request.GET.get('capitalize', 'off')
    if capitalize=="on":
        analyzed = text.upper()
        params = {'purpose':'Capitalized Text','analyzed':analyzed}

        return render(request,'analyzed.html',params)
    return HttpResponse("error")

 