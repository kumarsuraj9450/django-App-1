from django.shortcuts import render
from django.http import HttpResponse

from .forms import IMAGE_UPLOAD_FORM
# Create your views here.
from .models import image_file
def index(request):
    obj = {'message' : 'This is a classification app'}
    context = {
    'object' : obj
    }
    return render(request,'base.html',context)

# def add_image(request):
    """this is for pure django from"""
#     form=IMAGE_UPLOAD_FORM()

#     if request.method == 'POST':
#         form=IMAGE_UPLOAD_FORM(request.POST , request.FILES or None)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             image_file.objects.create(**form.cleaned_data)

#     context={
#     'form':form
#     } 

#     form=IMAGE_UPLOAD_FORM()
#     return render(request,'base.html',context)

def add_image(requests):
    """model form"""
    form=IMAGE_UPLOAD_FORM(requests.POST or None, requests.FILES or None)

    context = {'form':form, }
    
    if form.is_valid():
        form.save()
        form=IMAGE_UPLOAD_FORM()
        context={
        'form':form,'ob':image_file.objects.last()
        } 




    # image_file.objects.

    return render(requests,'vision.html',context)
