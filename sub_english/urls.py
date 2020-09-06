from django.urls import path
from . import views

urlpatterns = [
    path('english/textbook', views.eng_textbook, name='eng_textbook'),
    path('english/extras', views.eng_extras, name='eng_extras'),
    path('english/unit1', views.eng_unit_1, name='eng_unit_1'),
    path('english/unit2', views.eng_unit_2, name='eng_unit_2'),
    path('english/unit3', views.eng_unit_3, name='eng_unit_3'),
    path('english/unit4', views.eng_unit_4, name='eng_unit_4'),
    path('english/unit5', views.eng_unit_5, name='eng_unit_5'),
    path('english/unit6', views.eng_unit_6, name='eng_unit_6'),
]