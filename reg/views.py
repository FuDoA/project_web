from django.shortcuts import render
from reg.models import user
from django.http import HttpResponse
def index (request):
    return render(request,'reg/reg.html')

def check (request):
    user_id_check=request.GET['reg_id']
    if user.objects.filter(id=user_id_check)!=[]:
        return  HttpResponse('100')
    elif user.objects.filter(id=user_id_check)==[]:
        return HttpResponse('200')


def reg(request):
    reg_id=request.POST.get('reg_id')
    reg_salt =request.POST.get('reg_salt')
    reg_pswmd5=request.POST.get('reg_pswmd5')
    if user.objects.filter(id=user_id_check)!=[]:
        return HttpResponse('400')
    else:
        user.objects.create(id=reg_id,salt=reg_salt,pswmd5=reg_pswmd5)
        return hHttpResponse('300')
