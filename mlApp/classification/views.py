from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    obj ={'message' : 'Hello Bootstrap'}
    context = {
    'object' : obj
    }
    return render(request,'base.html',context)