from  django.urls import include, path
from . import views
from . import api

urlpatterns= [
    path('', views.GeneList.as_view(), name='index'),
    path('gene/<int:pk>', views.GeneDetail.as_view(), name='gene'),
    path('delete/<int:pk>', views.GeneDelete.as_view(),name='delete'),
    path('create_ec/', views.create_ec, name='create_ec'),
    path('create_gene/', views.GeneCreate.as_view(), name='create_gene'),
    path('update/<int:pk>', views.GeneUpdate.as_view(), name='update'),
    path('api/gene/<int:pk>', api.GeneDetail.as_view(), name="gene_api"),
    path('api/genes',api.GeneList.as_view(), name="genes_api")
]