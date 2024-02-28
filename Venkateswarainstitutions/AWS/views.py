from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def aws(request):
    return render(request,'AWS/aws.html')

def jen(request):
    return render(request,'AWS/jenkins.html')