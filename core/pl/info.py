from django.db import models
from dynamicModelingPOC import settings

# Create your models here.
class Info_PL(models.Model):
    id = models.IntegerField(primary_key=True)
    banner = models.CharField(null=False, max_length=25)

    class Meta:
        db_table = 'info'
        # decorate if schema specified
        if (hasattr(settings, 'DB_SCHEMA_NAME')) and settings.DB_SCHEMA_NAME == 'ddb_pl':
            db_table = f'[{settings.DB_SCHEMA_NAME}].[{db_table}]'