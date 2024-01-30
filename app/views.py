from django.shortcuts import render
from app. models import *
# Create your views here.
def equijoin(request):
    empobjects=Emp.objects.select_related('deptno').all()
    empobjects=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    empobjects=Emp.objects.select_related('deptno').filter(deptno__dname='accounting')
    empobjects=Emp.objects.select_related('deptno').filter(deptno__loc='dallas')
    empobjects=Emp.objects.select_related('deptno').filter(deptno=10)
    empobjects=Emp.objects.select_related('deptno').filter(sal__gt=2500)
    empobjects=Emp.objects.select_related('deptno').all()[:5:]
    empobjects=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    empobjects=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    empobjects=Emp.objects.select_related('deptno').all()[5:10:]
    empobjects=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    empobjects=Emp.objects.select_related('deptno').filter(ename='smith')
    d={'empobjects':empobjects}
    return render(request,'equijoin.html',d)