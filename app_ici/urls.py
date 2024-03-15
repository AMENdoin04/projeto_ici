from . import views
from django.urls import path

urlpatterns = [
    path('', views.lista_de_eventos, name="index"),
    path('eventos/', views.eventos_listados, name="eventos_list"),
    path('dizimos/', views.dizimos, name="dizimos_page"),
]