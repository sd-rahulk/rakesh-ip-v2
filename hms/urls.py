from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', views.list_doctors, name='list_doctors'),
    path('doctors/', views.doctors, name='doctors'),  # Example URL pattern
    path('doctors/add/', views.add_doctor, name='add_doctor'),
    path('patients/', views.list_patients, name='list_patients'),
    path('patients/add/', views.add_patient, name='add_patient'),
    path('appointments/', views.list_appointments, name='list_appointments'),
    path('appointments/add/', views.add_appointment, name='add_appointment'),
    path('doctors/<int:pk>/edit/', views.edit_doctor, name='edit_doctor'),
    path('doctors/<int:pk>/delete/', views.delete_doctor, name='delete_doctor'),
]
