from django.shortcuts import render
from myapp.form import studentform
def home(request):
    stud=studentform
    return render(request,'index.html',{'form':stud})
