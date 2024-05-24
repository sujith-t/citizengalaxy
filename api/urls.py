from django.urls import path

from . import views

urlpatterns = [
    path('v1/galaxy/classify', views.classify_galaxy, name='v1_galaxy_classification'),
    path("v1/catalog/search/<str:option>/<str:identifier>", views.basic_search, name='v1_basic_search'),
    path("v1/catalog/search/ra-dec", views.ra_dec_search, name='v1_ra_dec_search'),
    path("v1/catalog/<str:option>/<str:identifier>/detail", views.catalog_details, name='v1_detail'),
    #path("v1/catalog/iauname/<str:name>/detail", name='v1_iauname_detail')
]
