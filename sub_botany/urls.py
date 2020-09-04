from django.urls import path
from . import views

urlpatterns = [
    path('botany/chapter1', views.botany_chapter_1, name='botany_chapter_1'),
]