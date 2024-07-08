from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from webapp.service.search import GalaxyLocatorServiceImpl
from .serializers import ClassifySerializer
from .service.classifier import ClassifierFactory
from webapp.service.stats import StatisticalServiceImpl

# @author Sujith T
# Deus et Scientia Erit Pactum Meum 2024

classifier = ClassifierFactory.fetch_classifier()


@api_view(["POST"])
def classify_galaxy(request):
    serializer = ClassifySerializer(data=request.data)

    if serializer.is_valid():
        clazz = classifier.predict_galaxy_class(serializer.data)
        return Response([clazz], status=200)
    else:
        return Response({"message": "Invalid data posted", "status": 400, "errors": serializer.errors}, status=400)


@api_view(["GET"])
def basic_search(request, option, identifier):
    if option not in ['id', 'iauname'] or identifier is None:
        return Response({"message": "Invalid search parameters", "status": 400,
                         "errors": ["provided values: %s (option), %s (identifier)" % (option, identifier)]},
                        status=400)

    search_param = {"search_value": identifier, "search_option": "obj_id"}
    if option != "id":
        search_param["search_option"] = option

    locator = GalaxyLocatorServiceImpl()
    items = locator.search(search_param, is_json=True)
    json_obj = None
    if len(items) > 0:
        json_obj = items[0]

    if json_obj is None:
        return Response(status=204)

    return JsonResponse(json_obj, safe=False)


@api_view(["POST"])
def ra_dec_search(request):
    post_data = request.data
    if "ra" not in post_data or "dec" not in post_data:
        return Response({"message": "Invalid search parameters for RA/DEC", "status": 400,
                         "errors": ["provided values: %s " % post_data]}, status=400)

    post_data["search_option"] = "ra_dec"
    locator = GalaxyLocatorServiceImpl()

    items = locator.search(post_data, is_json=True)
    http_code = 200
    if len(items) == 0:
        http_code = 204

    return Response(items, status=http_code)


@api_view(["POST"])
def feature_values_per_class(request):
    post_data = dict(request.data)
    if "features[]" in post_data.keys():
        post_data['features'] = post_data["features[]"]
        post_data.pop("features[]")

    if type(post_data['class']) is list:
        post_data['class'] = post_data['class'][0]

    stat_service = StatisticalServiceImpl()
    output = stat_service.feature_values(post_data)

    if output is None:
        return Response(status=400)

    return Response(output)


@api_view(["GET"])
def catalog_details(request, option, identifier):
    if option not in ['id', 'iauname'] or identifier is None:
        return Response({"message": "Invalid search parameters", "status": 400,
                         "errors": ["provided values: %s (option), %s (identifier)" % (option, identifier)]},
                        status=400)

    search_param = {"search_value": identifier, "search_option": "obj_id"}
    if option != "id":
        search_param["search_option"] = option

    locator = GalaxyLocatorServiceImpl()
    item = locator.get_details(search_param, is_json=True)

    http_code = 200
    if item is None:
        http_code = 204

    return Response(item, status=http_code)


@api_view(["GET"])
def class_counts(request):
    stat_service = StatisticalServiceImpl()
    counts = stat_service.class_counts()
    return Response(counts)
