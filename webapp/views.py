import pandas as pd
from django.shortcuts import render

from citizengalaxy.settings import STATICFILES_DIRS
from .service.search import GalaxyLocatorServiceImpl
from .service.stats import StatisticalServiceImpl


# Create your views here.
def index(request):
    return render(request, 'index.html')


def statistics(request):
    stats_service = StatisticalServiceImpl()
    data_path = str(STATICFILES_DIRS.__getitem__(0)) + "/data"
    df = pd.read_csv(data_path + "/feature_min_max.csv")
    view_data = {'classes': stats_service.htf_sequence(), 'features': df['feature']}

    return render(request, 'statistics.html', view_data)


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
                     "search_value": request.POST.get('search_value').strip()}
        if post_data["search_option"] == "ra_dec":
            post_data["ra"] = request.POST.get('ra').strip()
            post_data["dec"] = request.POST.get('dec').strip()

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
    search_param = {"search_value": obj_id, "search_option": "obj_id"}
    view_data["galaxy"] = locator.get_details(search_param)

    return render(request, 'catalog_detail.html', view_data)
