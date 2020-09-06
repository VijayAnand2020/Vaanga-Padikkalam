from django.urls import path
from . import views

urlpatterns = [
    path('chemistry/textbook', views.chem_textbook, name='chem_textbook'),
    path('chemistry/chapter1', views.chem_chapter_1, name='chem_chapter_1'),
    path('chemistry/chapter2', views.chem_chapter_2, name='chem_chapter_2'),
    path('chemistry/chapter3', views.chem_chapter_3, name='chem_chapter_3'),
    path('chemistry/chapter4', views.chem_chapter_4, name='chem_chapter_4'),
    path('chemistry/chapter5', views.chem_chapter_5, name='chem_chapter_5'),
    path('chemistry/chapter6', views.chem_chapter_6, name='chem_chapter_6'),
    path('chemistry/chapter7', views.chem_chapter_7, name='chem_chapter_7'),
    path('chemistry/chapter8', views.chem_chapter_8, name='chem_chapter_8'),
    path('chemistry/chapter9', views.chem_chapter_9, name='chem_chapter_9'),
    path('chemistry/chapter10', views.chem_chapter_10, name='chem_chapter_10'),
    path('chemistry/chapter11', views.chem_chapter_11, name='chem_chapter_11'),
    path('chemistry/chapter12', views.chem_chapter_12, name='chem_chapter_12'),
    path('chemistry/chapter13', views.chem_chapter_13, name='chem_chapter_13'),
    path('chemistry/chapter14', views.chem_chapter_14, name='chem_chapter_14'),
    path('chemistry/chapter15', views.chem_chapter_15, name='chem_chapter_15'),
]