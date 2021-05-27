from django.shortcuts import render
from django.shortcuts import redirect
from . import models

def index(request):
    return render(request, 'account/top.html')

def user_create(request):
    #リクエストメソッドがGETならユーザー登録画面に遷移
    if request.method == 'GET':
        return render(request, 'account/user_create.html')


def user_list(request):
    queryset = models.User.objects.all()
    context = {
        'user_list':queryset
    }
    return render(request, 'account/user_list.html', context)

def user_detail(request, pk):
    queryset = models.User.objects.get(pk=pk)
    context = {
        'user':queryset
    }
    return render(request, 'account/user_detail.html', context)
