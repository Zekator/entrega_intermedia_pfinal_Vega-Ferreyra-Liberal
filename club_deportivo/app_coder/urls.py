from django.urls import path

from app_coder import views


app_name='app_coder'
urlpatterns = [
    path('', views.index, name='Inicio'),
    path('profesor/', views.profesors, name='Profesores'),
    path('sport/', views.sport, name='Deportes'),
    path('partner/', views.partner, name='Socios'),
    path('contac_us/', views.contact_us, name='Contacto'),
    path('profesorFormulario/', views.profesorsFormulario, name='ProfesoresFormulario'),
    path('profesor-django-forms', views.profesor_forms_django, name='ProfesorDjangoForms'),
]