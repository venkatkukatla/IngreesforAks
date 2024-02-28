from django.contrib import admin

from AZURE.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','fathername','contact']


# Register your models here.

admin.site.register(Student,StudentAdmin)

