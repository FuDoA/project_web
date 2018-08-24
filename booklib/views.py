from django.shortcuts import render
from booklib.models import book
# Create your views here.

def index (request):
    books=book.objects.all()
    return  render(request,'booklib/booklib.html',{'books':books})