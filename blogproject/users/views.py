from django.shortcuts import render,redirect
from django.contrib import messages
from users.forms import RegisteForm #不用管爆红
# Create your views here.
def registe(request):
    if request.method=='GET':
        form=RegisteForm()
    else:
        form=RegisteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'恭喜你注册成功！')
            return redirect('/')
    return render(request,'form.html',context={
        'form':form,
        'little_title':'注册用户'
    })
def success(request):
    msg=request.GET.get('msg')
    messages.add_message(request,messages.SUCCESS,msg)
    return redirect('/')