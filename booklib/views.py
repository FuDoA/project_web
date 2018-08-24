from django.shortcuts import render
from booklib.models import book
from django.db.models import Q
# Create your views here.

def index (request):
    books=book.objects.all()
    return  render(request,'booklib/booklib.html',{'books':books})

def searchbook (request):
    wantbook = request.GET['searchbook']
    gotbook = book.objects.filter(Q(book_name__icontains=wantbook)|Q(book_author__icontains=wantbook))
    return  render(request,'booklib/searchbook.html',{'books':gotbook})

