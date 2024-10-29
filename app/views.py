from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.forms import *

def basicStudentDjForms(request):
    ESFO=StudentForm()#EmptyStudentFormObject
    d={'ESFO':ESFO}
     
    if request.method=="POST":
        SFDO=StudentForm(request.POST)#StudentFormDataObject
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))

        else:
            return HttpResponse('Invalid Data')

    return render(request, 'basicStudentDjForms.html', d)