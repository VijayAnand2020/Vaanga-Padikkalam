from django.urls import path
from . import views

urlpatterns = [
    path('botany/chapter1', views.botany_chapter_1, name='botany_chapter_1'),
    path('botany/chapter2', views.botany_chapter_2, name='botany_chapter_2'),
    path('botany/chapter3', views.botany_chapter_3, name='botany_chapter_3'),
    path('botany/chapter4', views.botany_chapter_4, name='botany_chapter_4'),
    path('botany/chapter5', views.botany_chapter_5, name='botany_chapter_5'),
    path('botany/chapter6', views.botany_chapter_6, name='botany_chapter_6'),
    path('botany/chapter7', views.botany_chapter_7, name='botany_chapter_7'),
    path('botany/chapter8', views.botany_chapter_8, name='botany_chapter_8'),
    path('botany/chapter9', views.botany_chapter_9, name='botany_chapter_9'),
    path('botany/chapter10', views.botany_chapter_10, name='botany_chapter_10'),
]