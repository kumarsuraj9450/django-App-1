from django.shortcuts import render
from django.http import HttpResponse

from .forms import IMAGE_UPLOAD_FORM
# Create your views here.

def index(request):
    obj = {'message' : 'This is a classification app'}
    context = {
    'object' : obj
    }
    return render(request,'base.html',context)