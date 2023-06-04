from django.urls import path

from manufacturer.views import get_manuf

urlpatterns = [
    path('task2/<int:contract_id>', get_manuf, name='get_all_manuf_by_id_contract')
]