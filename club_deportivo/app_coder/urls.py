from django.urls import path

from app_coder import views


app_name='app_coder'
urlpatterns = [
    path('', views.index, name='Inicio'),
    path('profesor/', views.profesors, name='Profesores'),
    path('sport/', views.sport, name='Deportes'),
    path('partner/', views.partner, name='Socios'),

    #path('index-2', views.index2),
    #path('get-course-2/<int:id>/', views.get_course2),
    #path('post-course-2/<str:name>/<int:code>/', views.post_course2),
    #path('all-courses-2/', views.all_courses2),

    #path('cursos', views.cursos),
]