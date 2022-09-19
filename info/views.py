from django.shortcuts import render
from rest_framework import viewsets
from .models import Info_PL, Info_MX
from .serializers import InfoSerializer
from dynamicModelingPOC import settings
from common.utilities import get_model_name


# Create your views here.

class InfoViewSet(viewsets.ModelViewSet):
    serializer_class = InfoSerializer
    modelName = get_model_name()
    queryset = modelName.objects.filter(banner='Banner2').values()


