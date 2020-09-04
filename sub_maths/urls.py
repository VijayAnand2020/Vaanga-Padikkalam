from django.urls import path
from . import views

urlpatterns = [
    path('maths/chapter1', views.maths_chapter_1, name='maths_chapter_1'),
    path('maths/chapter2', views.maths_chapter_2, name='maths_chapter_2'),
]