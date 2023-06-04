from django.contrib import admin

from catalog.models import LoanApplication, Product


@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    """"""


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """"""
