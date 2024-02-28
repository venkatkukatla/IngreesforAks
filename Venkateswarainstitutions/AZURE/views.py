from django.shortcuts import render

from django.http import HttpResponse

from AZURE.models import Student



# Create your views here.

def homepage(request):
    return render(request,'index.html')

def azure(request):
    values={"name":"azure","duration":"days60","cloud":"Azure cloud"}
    return render(request,'AZURE/azure.html',values)

def ado(request):
    #select all the records from the table
    result = Student.objects.all(); #select * from table
    #store dictonary students
    students = {'allstudents':result}
    return render(request,'AZURE/admission.html',students);

