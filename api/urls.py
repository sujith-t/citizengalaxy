from django.urls import path

from . import views

urlpatterns = [
    path('v1/galaxy/classify', views.classify_galaxy, name='v1_galaxy_classification')
    #path('v1/catalog/search/{iauname|id}', , name='v1_search_basic'),
    #path('v1/catalog/search/advance', , name='v1_search_advance'),
    #path('v1/statstics/*', , name='v1_galaxy_classification'),
]