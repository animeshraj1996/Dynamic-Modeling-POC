from dataclasses import fields
from rest_framework import serializers
from .models import Info_PL, Info_MX
from dynamicModelingPOC import settings

class InfoSerializer(serializers.ModelSerializer):
    if settings.DB_SCHEMA_NAME == 'ddb_mx':
        class Meta:
            model = Info_MX
            fields = '__all__'
    else:
        class Meta:
            model = Info_PL
            fields = '__all__'