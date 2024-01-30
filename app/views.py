from django.shortcuts import render
from app. models import *
# Create your views here.
def equijoin(request):
    empobjects=Emp.objects.select_related('deptno').all()
    d={'empobjects':empobjects}
    return render(request,'equijoin.html',d)