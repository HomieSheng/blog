from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic import TemplateView


def view1(request):
    if request.method == 'GET':
        return HttpResponse('发起了GET请求')
    else:
        return HttpResponse('发起了POST请求')




def view5(request):
    return render(request, 'class/test.html')


class view6(View):

    def get(self, request, *arg, **kwargs):
        return HttpResponse('发起了GET请求')

    def post(self, request, *arg, **kwargs):
        return HttpResponse('发起了POST请求')


def view7(TemplateView):
    template_name = 'class/test.html'


class view2():
    @staticmethod
    def as_view():
        return view1


class view3(View):
    def get(self, request, *arg, **kwargs):
        return HttpResponse('发起了GET请求')

    def post(self, request, *arg, **kwargs):
        return HttpResponse('发起了POST请求')


class GetMixin:
    def get(self, request, *arg, **kwargs):
        return HttpResponse('发起了GET请求')


class view4(GetMixin, View):
    def post(self, request, *arg, **kwargs):
        return HttpResponse('发起了POST请求')
