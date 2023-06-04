from django.db import models
from testWork.base_model import BaseDjangoModel, BaseModelNamedEntities


class Product(BaseModelNamedEntities):
    """модель для сущности товар"""
    manufacturer = models.ForeignKey('manufacturer.Manufacturer', related_name='products',
                                     on_delete=models.CASCADE)  # todo (не указаны правила)
    loan_application = models.ForeignKey('LoanApplication', related_name='products', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class LoanApplication(BaseDjangoModel):
    """модель для сущности кредитная заявка"""
    contract = models.ForeignKey('manufacturer.Contract', related_name='applications', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'кредитная заявка'
        verbose_name_plural = 'кредитные заявки'

    def __str__(self):
        return f'{self.id}-{self.contract}'
