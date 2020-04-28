from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('conciertos/<int:id>', views.concierto, name="concierto"),
    path('grupos/', views.grupos, name="grupos"),
    path('grupos/<int:id>', views.grupo, name="grupo"),
    path('musicos/', views.musicos, name="musicos"),
    path('musicos/<int:id>', views.musico, name="musico"),
]
