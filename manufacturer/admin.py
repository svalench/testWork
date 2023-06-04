from django.contrib import admin

from manufacturer.models import Manufacturer, Contract


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    """"""


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    """"""
