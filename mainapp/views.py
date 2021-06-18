from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers

# Create your views here.
from mainapp.models import Product


def index(request):
    return render(request, 'mainapp/index.html', {})

def data_api(request):
    data = serializers.serialize("json", Product.objects.all())
    return JsonResponse(data=data, safe=False)
