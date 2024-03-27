from django.shortcuts import render
from .service.search import GalaxyLocatorServiceImpl

# Create your views here.
def index(request):
    return render(request, 'index.html')


def statistics(request):
    return render(request, 'statistics.html')


def classify(request):
    return render(request, 'classify.html')


def catalog(request):
    page_no = request.GET.get('page', 1)
    locator = GalaxyLocatorServiceImpl()
    result = locator.get_page_result(page_no)

    return render(request, 'catalog.html', {'catalog': result})
