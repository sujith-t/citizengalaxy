from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def statistics(request):
    return render(request, 'statistics.html')

def classify(request):
    return render(request, 'classify.html')
