from django.shortcuts import render
from django.core.paginator import Paginator
from .models import GalaxyCatalogModel


# Create your views here.
def index(request):
    return render(request, 'index.html')


def statistics(request):
    return render(request, 'statistics.html')


def classify(request):
    return render(request, 'classify.html')


def catalog(request):
    paginator = Paginator(GalaxyCatalogModel.objects.all(), 10)
    page1 = paginator.page(1)
    print(page1.object_list)
    return render(request, 'catalog.html')
