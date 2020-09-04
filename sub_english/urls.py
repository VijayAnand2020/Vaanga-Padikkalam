from django.urls import path
from . import views

urlpatterns = [
    path('english/unit1', views.eng_unit_1, name='eng_unit_1'),
]