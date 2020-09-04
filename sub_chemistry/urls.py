from django.urls import path
from . import views

urlpatterns = [
    path('chemistry/chapter1', views.chem_chapter_1, name='chem_chapter_1'),
]