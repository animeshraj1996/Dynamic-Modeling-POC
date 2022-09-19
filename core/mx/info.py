from django.db import models
from dynamicModelingPOC import settings


class Info_MX(models.Model):
    id = models.IntegerField(primary_key=True)
    channel = models.CharField(null=False, max_length=25)

    class Meta:
        db_table = 'info'
        # decorate if schema specified
        if (hasattr(settings, 'DB_SCHEMA_NAME')) and settings.DB_SCHEMA_NAME == 'ddb_mx':
            db_table = f'[{settings.DB_SCHEMA_NAME}].[{db_table}]'
