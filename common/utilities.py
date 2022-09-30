from operator import ge
import sys
sys.path.append('../')
from info.models import Info_PL, Info_MX


def get_model_name(region_name):
    if region_name == 'mx':
        modelName = Info_MX
    else:
        modelName = Info_PL
    return modelName