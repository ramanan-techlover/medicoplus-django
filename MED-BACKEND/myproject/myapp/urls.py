from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('doctors/', views.doctors, name='doctors'),
    path('login/', views.login, name='login'),
    path('healthcard/', views.healthcard, name='healthcard'),
    path('medicine/', views.medicine, name='medicine'),
    path('laboratory/', views.laboratory, name='laboratory'),
    path('onlineconsultation/', views.onlineconsultation, name='onlineconsultation'),
    path('psychiatry/', views.psychiatry, name='psychiatry'),
    path('gynecology/', views.gynecology, name='gynecology'),
    path('pulmonology/', views.pulmonology, name='pulmonology'),
    path('orthopedics/', views.orthopedics, name='orthopedics'),
    path('pediatrics/', views.pediatrics, name='pediatrics'),
    path('osteology/', views.osteology, name='osteology'),
    path('blog1/', views.blog1, name='blog1'),
    path('blog2/', views.blog2, name='blog2'),
    path('blog3/', views.blog3, name='blog3'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('join_as_doctor/', views.join_as_doctor, name='join_as_doctor'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('add/', views.add_patient, name='add'),
    path('nfc-scan/<str:card_id>/', views.nfc_scan, name='nfc_scan'),
]
