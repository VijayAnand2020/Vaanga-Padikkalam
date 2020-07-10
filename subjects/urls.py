from django.urls import path
from . import views

urlpatterns = [
    path('tamil/', views.tamil, name='tamil'),
    path('english/', views.english, name='english'),
    path('maths/', views.maths, name='maths'),
    path('physics/', views.physics, name='physics'),
    path('chemistry/', views.chemistry, name='chemistry'),
    path('csc/', views.csc, name='csc'),
    # path('biology/', views.biology, name='menu'),
    path('botany/', views.botany, name='botany'),
    path('zoology/', views.zoology, name='zoology'),
]
