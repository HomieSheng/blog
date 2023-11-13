from django.urls import path
from . import class_views
from django.views.generic import TemplateView
urlpatterns = [
    path('view1/', class_views.view1),
    path('view2/', class_views.view2.as_view()),
    path('view3/', class_views.view3.as_view()),
    path('view4/', class_views.view4.as_view()),
    path('view5/', class_views.view5),
    path('view6/', class_views.view6.as_view()),
    path('view7/', TemplateView.as_view(template_name='class/test.html')),
]


