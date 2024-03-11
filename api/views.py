from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ClassifySerializer
from .service.classifier import RandomForestClassifierImpl

# @author Sujith T
# Deus et Scientia Erit Pactum Meum 2024

classifier = RandomForestClassifierImpl()

@api_view(["POST"])
def classify_galaxy(request):
    serializer = ClassifySerializer(data=request.data)

    if serializer.is_valid():
        clazz = classifier.predict_galaxy_class(serializer.data)
        return Response([clazz], status=200)
    else:
        return Response({"message": "Invalid data posted", "status": 400, "errors": serializer.errors})
