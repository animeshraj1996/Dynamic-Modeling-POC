import sys
sys.path.append('../')
from config.database import DB_SCHEMA_NAME
from info.models import Info_PL, Info_MX


def get_model_name():
    if DB_SCHEMA_NAME == 'ddb_mx':
        modelName = Info_MX
    else:
        modelName = Info_PL
    return modelName