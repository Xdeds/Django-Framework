from django.contrib import admin
from .models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'full_name')

admin.site.register(Student, StudentAdmin)