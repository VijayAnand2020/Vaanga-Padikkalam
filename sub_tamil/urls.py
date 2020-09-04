from django.urls import path
from . import views

urlpatterns = [
    path('tamil/unit1', views.tam_unit_1, name='tam_unit_1'),
]