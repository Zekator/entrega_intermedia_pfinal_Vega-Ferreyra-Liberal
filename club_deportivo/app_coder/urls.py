from django.urls import path

from app_coder import views


app_name='app_coder'
urlpatterns = [
    path('', views.index, name='Inicio'),
    path('profesors/', views.profesors, name='Profesores'),
    path('sport/', views.sport, name='Deportes'),
    path('partner/', views.partner, name='Socios'),
    path('profesor_forms', views.ProfesorForm.as_view(), name='ProfesorForms'),
    path('profesor/<int:pk>/list',views.ProfesorList.as_view(), name='profesor_list'),
    path('profesor/<int:pk>/create',views.ProfesorCreate.as_view(), name='profesor-create'),
    path('profesor/<int:pk>/delete',views.ProfesorDelete.as_view(), name='profesor-delete'),
    path('profesor/<int:pk>/update',views.ProfesorUpdate.as_view(), name='profesor-update'),
        ]