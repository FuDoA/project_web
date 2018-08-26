from django.shortcuts import render
from reg.models import user
from django.http import HttpResponse


def index(request):
    return render(request,'reg/reg.html')


def check(request):
    user_id_check = request.GET.get('reg_id')
    user_result = user.objects.filter(id=user_id_check)
    if user_result:
        return HttpResponse(100)
    else:
        return HttpResponse(200)


def reg(request):
    reg_id = request.POST.get('reg_id')
    reg_salt = request.POST.get('reg_salt')
    reg_pswmd5 = request.POST.get('reg_pswmd5')
    user_result = user.objects.filter(id=reg_id)
    if user_result:
        return HttpResponse(400)
    else:
        user.objects.create(id=reg_id, salt=reg_salt, pswmd5=reg_pswmd5)
        return HttpResponse(300)
