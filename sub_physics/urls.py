from django.urls import path
from . import views

urlpatterns = [
    path('physics/textbook', views.phy_texbook, name='phy_textbook'),
    path('physics/chapter1', views.phy_chapter_1, name='phy_chapter_1'),
    path('physics/chapter2', views.phy_chapter_2, name='phy_chapter_2'),
    path('physics/chapter3', views.phy_chapter_3, name='phy_chapter_3'),
    path('physics/chapter4', views.phy_chapter_4, name='phy_chapter_4'),
    path('physics/chapter5', views.phy_chapter_5, name='phy_chapter_5'),
    path('physics/chapter6', views.phy_chapter_6, name='phy_chapter_6'),
    path('physics/chapter7', views.phy_chapter_7, name='phy_chapter_7'),
    path('physics/chapter8', views.phy_chapter_8, name='phy_chapter_8'),
    path('physics/chapter9', views.phy_chapter_9, name='phy_chapter_9'),
    path('physics/chapter10', views.phy_chapter_10, name='phy_chapter_10'),
    path('physics/chapter11', views.phy_chapter_11, name='phy_chapter_11'),
]