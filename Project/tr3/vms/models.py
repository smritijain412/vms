from django.db import models
from .validators import validate_file_extension

# Create your models here.
DESIGNATION = (("HR", "HR"), ("Employee", "Employee"))


class Employee(models.Model):
    uname = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    password = models.CharField(max_length=100)
    re_password = models.CharField(max_length=100)
    designation = models.CharField(choices=DESIGNATION, max_length=50)

    def __str__(self):
        return self.name

    @property
    def visits(self):
        visit_count = self.visit_set.all().count()
        return str(visit_count)


class Visitor(models.Model):
    CATEGORY = (('Student', 'Student'), ('Guest', 'Guest'))

    name = models.CharField(max_length=150)
    contact = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    purpose = models.CharField(max_length=250)
    photo = models.ImageField(upload_to="visitor/photo",
                              validators=[validate_file_extension])
    category = models.CharField(max_length=50, choices=CATEGORY)
    date_visited = models.DateTimeField(auto_now_add=True)
    host = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Visit(models.Model):
    STATUS = (('Pending', 'Pending'), ('Done', 'Done'))
    employee = models.ForeignKey(
        Employee, null=True, on_delete=models.SET_NULL)
    visitor = models.ForeignKey(Visitor, null=True, on_delete=models.SET_NULL)
    date_visited = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)


# class student(models.Model):
#     name = models.CharField(max_length=150)
#     contact = models.CharField(max_length=20)
#     email = models.EmailField(max_length=100)
#     purpose = models.CharField(required=False)
#     photo = models.ImageField(upload_to="student/photo",
#                               validators=[validate_file_extension])

#     date_visited = models.DateTimeField(auto_now_add=True)

class events(models.Model):
    event_name = models.CharField(max_length=250)
    event_date = models.DateTimeField(auto_now_add=True)
