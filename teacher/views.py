from django.shortcuts import render
from .models import Teacher
from django.http import JsonResponse
# Create your views here.

def get_all(request):
    if request.method=="GET":
        all_date= Teacher.objects.all()
        result=[]
        for teacher in all_date:
             result.append({"id":teacher.id,"teacher_name":teacher.first_name})
        return JsonResponse({"date":result})

def get_by_id(request,student_id):
    if request.method=="GET":
        try:
            date=Teacher.objects.get(id=student_id)
        except Teacher.DoesNotExists:
            return JsonResponse({"msg": "NOT FOUND"})
        return JsonResponse({"id":date.id,"teacher_name":date.first_name})




