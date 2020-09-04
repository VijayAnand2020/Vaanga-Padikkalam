from django.urls import path
from . import views

urlpatterns = [
    path('zoology/chapter1', views.zoology_chapter_1, name='zoology_chapter_1'),
]