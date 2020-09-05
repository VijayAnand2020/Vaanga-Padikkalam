from django.urls import path
from . import views

urlpatterns = [
    path('zoology/chapter1', views.zoology_chapter_1, name='zoology_chapter_1'),
    path('zoology/chapter2', views.zoology_chapter_2, name='zoology_chapter_2'),
    path('zoology/chapter3', views.zoology_chapter_3, name='zoology_chapter_3'),
    path('zoology/chapter4', views.zoology_chapter_4, name='zoology_chapter_4'),
    path('zoology/chapter5', views.zoology_chapter_5, name='zoology_chapter_5'),
    path('zoology/chapter6', views.zoology_chapter_6, name='zoology_chapter_6'),
    path('zoology/chapter7', views.zoology_chapter_7, name='zoology_chapter_7'),
    path('zoology/chapter8', views.zoology_chapter_8, name='zoology_chapter_8'),
    path('zoology/chapter9', views.zoology_chapter_9, name='zoology_chapter_9'),
    path('zoology/chapter10', views.zoology_chapter_10, name='zoology_chapter_10'),
    path('zoology/chapter11', views.zoology_chapter_11, name='zoology_chapter_11'),
    path('zoology/chapter12', views.zoology_chapter_12, name='zoology_chapter_12'),
]