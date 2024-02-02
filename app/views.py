from django.shortcuts import render
from app. models import *
from django.db.models.functions import Length
from django.db.models import Q
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

def selfjoin(request):
    empmgrobjects=Emp.objects.select_related('mgr').all()
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__gt=1000)
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__lt=1000)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='king')
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__isnull=False)
    empmgrobjects=Emp.objects.select_related('mgr').filter(ename__endswith='th')
    empmgrobjects=Emp.objects.select_related('mgr').filter(ename__startswith='a')
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__gte=2000)
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__lte=3000)
    empmgrobjects=Emp.objects.select_related('mgr').filter(ename__in=('smith','allen'))
    empmgrobjects=Emp.objects.select_related('mgr').filter(ename='blake')
    empmgrobjects=Emp.objects.select_related('mgr').order_by('-sal')
    empmgrobjects=Emp.objects.select_related('mgr').order_by('sal')
    empmgrobjects=Emp.objects.select_related('mgr').order_by(Length('ename').desc())
    d={'empmgrobjects':empmgrobjects}
    return render(request,'selfjoin.html',d)

def emp_mgr_dept(request):
    emdobjects=Emp.objects.select_related('deptno','mgr').all()
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='research')
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='blake')
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(ename='allen')
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(ename__startswith='a')
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(ename__endswith='th')
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(sal__gte=3000)
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(sal__lte=3000)
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(ename='martin')
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(job__in=('manager','analyst'))
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(ename__in=('smith','allen'))
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=True)
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=False)
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=True)
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(deptno__in=(10,20))
    emdobjects=Emp.objects.select_related('deptno','mgr').order_by('-comm')
    emdobjects=Emp.objects.select_related('deptno','mgr').order_by('comm')
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='sales',ename='allen')
    emdobjects=Emp.objects.select_related('deptno','mgr').order_by('-sal')
    emdobjects=Emp.objects.select_related('deptno','mgr').order_by('sal')
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='research')|Q(mgr__ename='jones'))
    emdobjects=Emp.objects.select_related('deptno','mgr').order_by(Length('job').desc())
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=True)
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=False)
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(sal__lt=3000)
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(sal__gt=3000)
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(deptno=10)
    emdobjects=Emp.objects.select_related('deptno','mgr').order_by(Length('job'))
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(deptno__gt=10)
    emdobjects=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='sales')
    emdobjects=Emp.objects.select_related('deptno','mgr').all()[:5:]
    emdobjects=Emp.objects.select_related('deptno','mgr').all()[2:5:]



    d={'emdobjects':emdobjects}
    return render(request,'emp_mgr_dept.html',d)