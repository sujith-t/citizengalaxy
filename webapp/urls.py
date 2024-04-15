from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('statistics', views.statistics, name='statistics'),
    path('classify', views.classify, name='classify'),
    path('catalog', views.catalog, name='catalog'),
    path('catalog/<str:obj_id>/detail', views.catalog_details, name='catalog_detail')
]