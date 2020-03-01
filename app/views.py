from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'app/base.html',{'dict':'Hello I am from views.py'})