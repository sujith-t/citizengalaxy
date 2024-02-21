from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ClassifySerializer
from .service.classifier import GalaxyClassClassifier

# @author Sujith T
# In God We Trust 2024

model = GalaxyClassClassifier()

@api_view(["POST"])
def classify_galaxy(request):
    serializer = ClassifySerializer(data=request.data)

    if serializer.is_valid():
        model.predict_galaxy_class([])
        return Response("Sa", status=200)
    else:
        return Response({"message": "Invalid data posted", "status": 400, "errors": serializer.errors})
    # return JsonResponse({"message": "this is the first api - " + request.content_type})
