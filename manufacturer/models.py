from django.db import models
from testWork.base_model import BaseModelNamedEntities


class Manufacturer(BaseModelNamedEntities):
    """модель для сущности Производитель"""

    class Meta:
        verbose_name = 'производитель'
        verbose_name_plural = 'производители'


class Contract(BaseModelNamedEntities):
    """модель для сущности Контракт"""

    class Meta:
        verbose_name = 'контракт'
        verbose_name_plural = 'контракты'
