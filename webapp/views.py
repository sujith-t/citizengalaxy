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
    page_no = int(request.GET.get('page', 1))
    locator = GalaxyLocatorServiceImpl()
    result = []
    total_pages = 1

    if request.method == "GET":
        total_pages, result = locator.get_page_result(page_no)

    if request.method == "POST":
        print("posted",request.POST.get("ra"), request.method)

    return render(request, 'catalog.html', {'catalog': result, 'total_pages': total_pages, 'page_no': page_no})
