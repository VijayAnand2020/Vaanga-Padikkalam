from django.urls import path
from . import views

urlpatterns = [
    path('physics/chapter1', views.phy_chapter_1, name='phy_chapter_1'),
]