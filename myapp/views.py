
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserDeviceForm

from django.views.decorators import csrf


def create_user_device(request):
    if request.method == 'POST':
        form = UserDeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # 替换'success_url'为操作成功后的重定向地址
    else:
        form = UserDeviceForm()
    return render(request, 'user_device_form.html', {'form': form})

def success_url(request):
    return render(request, 'success.html')  # 操作成功后的页面


def index(request):
    return render(request, 'index.html')  # 猫主页

def index1(request):
    return render(request, 'index1.html')  # 狗主页

def dashboard(request):
    return render(request, 'dashboard.html')  # 仪表盘

def user_device_list(request):
    return render(request, 'user_device_list.html')  # 用户设备列表

def user_device_detail(request):
    return render(request, 'user_device_detail.html')  # 用户设备详情

def live(request):
    return render(request, 'live.html')  # 实时监控

def user_device_form(request):
    return render(request, 'user_device_form.html')  # 用户设备表单

def user_device_edit(request):
    return render(request, 'user_device_edit.html')  # 用户设备编辑

def user_device_delete(request):
    return render(request, 'user_device_delete.html')  # 用户设备删除

def user_device_create(request):
    return render(request, 'user_device_create.html')  # 用户设备创建

def user_device_update(request):
    return render(request, 'user_device_update.html')  # 用户设备更新

def search_form(request):  #get查询
    return render(request, 'info.html')
 
# 接收请求数据
# def search(request):  
#     request.encoding='utf-8'
#     if 'q' in request.GET and request.GET['q']:
#         message = '你搜索的内容为: ' + request.GET['q']
#     else:
#         message = '你提交了空表单'
#     return HttpResponse(message)

def search(request):  
    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = request.GET['q']
        user = User.objects.filter(name=message).values('userid', 'name', 'age', 'gender').first()
        if user:
            return render(request, 'user_detail.html', {'user': user})
        else:
            return HttpResponse('用户不存在')

 
# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)

from django.shortcuts import render, redirect
from .forms import UserForm

def user_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')

    else:
        form = UserForm()

    return render(request, 'orm_post.html', {'form': form})

def success_url(request):
    return render(request, 'success.html')

from django.shortcuts import redirect
from .models import User

def delete_user(request, name):
    user = User.objects.get(name=name)
    user.delete()
    return HttpResponse('删除成功！')



def status(request):
    return render(request, 'status.html')  # 状态