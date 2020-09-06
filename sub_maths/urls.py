from django.urls import path
from . import views

urlpatterns = [
    path('maths/textbook', views.maths_textbook, name='maths_textbook'),
    path('maths/chapter1', views.maths_chapter_1, name='maths_chapter_1'),
    path('maths/chapter2', views.maths_chapter_2, name='maths_chapter_2'),
    path('maths/chapter3', views.maths_chapter_3, name='maths_chapter_3'),
    path('maths/chapter4', views.maths_chapter_4, name='maths_chapter_4'),
    path('maths/chapter5', views.maths_chapter_5, name='maths_chapter_5'),
    path('maths/chapter6', views.maths_chapter_6, name='maths_chapter_6'),
    path('maths/chapter7', views.maths_chapter_7, name='maths_chapter_7'),
    path('maths/chapter8', views.maths_chapter_8, name='maths_chapter_8'),
    path('maths/chapter9', views.maths_chapter_9, name='maths_chapter_9'),
    path('maths/chapter10', views.maths_chapter_10, name='maths_chapter_10'),
    path('maths/chapter11', views.maths_chapter_11, name='maths_chapter_11'),
    path('maths/chapter12', views.maths_chapter_12, name='maths_chapter_12'),
]