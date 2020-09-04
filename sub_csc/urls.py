from django.urls import path
from . import views

urlpatterns = [
    path('csc/chapter1', views.csc_chapter_1, name='csc_chapter_1'),
]