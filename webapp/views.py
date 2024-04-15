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
    post_data = {}
    page_no = int(request.GET.get('page', 1))
    locator = GalaxyLocatorServiceImpl()
    result = []
    total_pages = 1

    if request.method == "GET":
        total_pages, result = locator.get_page_result(page_no)

    if request.method == "POST":
        post_data = {"search_option": request.POST.get('search_option'),
                     "search_value": request.POST.get('search_value')}
        if post_data["search_option"] == "ra_dec":
            post_data["ra"] = request.POST.get('ra')
            post_data["dec"] = request.POST.get('dec')

        result = locator.search(post_data)

    if page_no < 1 or page_no > total_pages:
        page_no = 1

    view_data = {'catalog': result, 'total_pages': total_pages, 'page_no': page_no, "is_searched": 0}
    if request.method == "POST" and request.POST.get('search_option') is not None:
        view_data["is_searched"] = 1

    view_data["post_data"] = post_data
    return render(request, 'catalog.html', view_data)


def catalog_details(request, obj_id):
    view_data = {}
    locator = GalaxyLocatorServiceImpl()
    view_data["galaxy"] = locator.get_details(obj_id)

    return render(request, 'catalog_detail.html', view_data)
