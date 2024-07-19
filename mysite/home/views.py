from django.shortcuts import render
from django.http import  HttpResponse,JsonResponse
from .models import *
from django.core import serializers


# Create your views here.

def home(request):
    return HttpResponse("hello")

def student(request):
    if request.method == "POST": 
        data=request.POST
        image = request.FILES.get('image') 
        name = data.get("name")
        age = data.get("age")
        email = data.get("email")
        address = data.get("address")
        print(name)
        print(age)
        print(email)
        print(address)
        print(image)

        Student.objects.create(name= name, age=age, email=email, address=address, image=image)

    querySet = Student.objects.all()
    print(querySet)
    context = {'students':querySet}
    return render(request,'student.html',context)

def getStudents(request):
    data  = list(Student.objects.values()) 
    return JsonResponse(data,safe = False) 

def delete_student(request,id):
    querySet = Student.objects.get(id=id)
    querySet.delete()
    return 