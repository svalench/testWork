
from django.http import JsonResponse

from manufacturer.models import Manufacturer


def get_manuf(request, contract_id):
    """само второе задание"""
    manufacturers = Manufacturer.objects.filter(products__loan_application__contract_id=contract_id).distinct()
    return JsonResponse({"manufacturers": list(manufacturers.values())})
