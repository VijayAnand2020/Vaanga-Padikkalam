# from django.urls import path
# from . import views

# urlpatterns = [
#     path('csc/chapter1', views.csc_chapter_1, name='csc_chapter_1'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('csc/chapter1', views.csc_chapter_1, name='csc_chapter_1'),
    path('csc/chapter2', views.csc_chapter_2, name='csc_chapter_2'),
    path('csc/chapter3', views.csc_chapter_3, name='csc_chapter_3'),
    path('csc/chapter4', views.csc_chapter_4, name='csc_chapter_4'),
    path('csc/chapter5', views.csc_chapter_5, name='csc_chapter_5'),
    path('csc/chapter6', views.csc_chapter_6, name='csc_chapter_6'),
    path('csc/chapter7', views.csc_chapter_7, name='csc_chapter_7'),
    path('csc/chapter8', views.csc_chapter_8, name='csc_chapter_8'),
    path('csc/chapter9', views.csc_chapter_9, name='csc_chapter_9'),
    path('csc/chapter10', views.csc_chapter_10, name='csc_chapter_10'),
    path('csc/chapter11', views.csc_chapter_11, name='csc_chapter_11'),
    path('csc/chapter12', views.csc_chapter_12, name='csc_chapter_12'),
    path('csc/chapter13', views.csc_chapter_13, name='csc_chapter_13'),
    path('csc/chapter14', views.csc_chapter_14, name='csc_chapter_14'),
    path('csc/chapter15', views.csc_chapter_15, name='csc_chapter_15'),
    path('csc/chapter16', views.csc_chapter_16, name='csc_chapter_16'),
]