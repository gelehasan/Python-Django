from  django.urls import include, path
from . import views


urlpatterns= [
    path('', views.index, name='index'),
    path('gene/<int:pk>', views.gene, name='gene'),
    path('delete/<int:pk>', views.delete,name='delete'),
    path('create_ec/', views.create_ec, name='create_ec'),
    path('create_gene/', views.create_gene, name='create_gene'),
    path('update/<int:pk>', views.GeneUpdate.as_view(), name='update')
]