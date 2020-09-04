from django.urls import path
from . import views

urlpatterns = [
    path('tamil/unit1', views.tam_unit_1, name='tam_unit_1'),
    path('tamil/unit2', views.tam_unit_2, name='tam_unit_2'),
    path('tamil/unit3', views.tam_unit_3, name='tam_unit_3'),
    path('tamil/unit4', views.tam_unit_4, name='tam_unit_4'),
    path('tamil/unit5', views.tam_unit_5, name='tam_unit_5'),
    path('tamil/unit6', views.tam_unit_6, name='tam_unit_6'),
    path('tamil/unit7', views.tam_unit_7, name='tam_unit_7'),
    path('tamil/unit8', views.tam_unit_8, name='tam_unit_8'),
]