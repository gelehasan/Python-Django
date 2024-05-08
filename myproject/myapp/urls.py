from django.urls import path
from . import views

urlpatterns=[
    path('simple',myapp.views.simple_view, name='simple')
    path('', views.index, name='index'),
]