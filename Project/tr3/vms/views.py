from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from .models import Visitor, Visit, Employee
from .forms import VisitForm
from .filters import VisitFilter
# Create your views here.


def home(request):
    visits = Visit.objects.all()
    employees = Employee.objects.all()

    total_employees = employees.count()

    total_visits = visits.count()
    done = visits.filter(status='Done').count()
    pending = visits.filter(status='Pending').count()

    context = {'visits': visits, 'employees': employees, 'total_employees': total_employees,
               'total_visits': total_visits, 'done': done, 'pending': pending}
    return render(request, 'vms/dashboard.html', context)


def visitors(request):
    visitors = Visitor.objects.all()
    return render(request, 'vms/visitors.html', {'visitors': visitors})


def employee_dash(request, pk):
    employee = Employee.objects.get(id=pk)
    visits = employee.visit_set.all()
    visits_count = visits.count()
    context = {'employee': employee, 'visits': visits,
               'visits_count': visits_count}
    return render(request, 'vms/employee_dash.html', context)


def createVisit(request, pk):
    employee = Employee.objects.get(id=pk)
    form = VisitForm(initial={'employee': employee})
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    # else:
    #     form = VisitForm()
    return render(request, 'vms/visit_form.html', {'form': form})


def updateVisit(request, pk):
    visit = Visit.objects.get(id=pk)
    form = VisitForm(instance=visit)
    if request.method == 'POST':
        form = VisitForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'vms/visit_form.html', {'form': form})


def deleteVisit(request, pk):
    visit = Visit.objects.get(id=pk)
    if request.method == 'POST':
        visit.delete()
        return redirect('/')

    return render(request, 'vms/delete_visit.html', {'visit': visit})


def employee(request):
    employee = Employee.objects.all()
    # visits = employee.visit_set.all()
    # visits_count = visits.count()
    # context = {'employee': employee, 'visits': visits,
    #            'visits_count': visits_count}
    return render(request, 'vms/employee.html', {'employee': employee})


# def createVisit_i(request, pk):
#     VisitFormSet = inlineformset_factory(
#         Employee, fields=('visitor', 'status'), extra=10)

#     employee = Employee.objects.get(id=pk)
#     formset = VisitFormSet(queryset=Visit.object.none(), instance=employee)

#     form = VisitForm(initial={'employee': employee})
#     if request.method == 'POST':
#         form = VisitForm(request.POST)
#         formset = VisitFormSet(request.POST, instance=employee)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     # else:
#     #     form = VisitForm()
#     return render(request, 'vms/visit_form.html', {'form': form})
