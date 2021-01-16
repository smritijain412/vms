from django.contrib import admin
from .models import Employee, Visitor, Visit
# Register your models here.

admin.site.register(Employee)
admin.site.register(Visitor)
admin.site.register(Visit)
# @admin.register(guest)
# class RegisterAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'contact', 'email',
#                     'purpose', 'photo', 'date_visited', 'host')
