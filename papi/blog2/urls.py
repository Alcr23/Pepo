from django.urls import path
from . import views
urlpatterns = [
    path('blog2/', views.muestra_datos, name='blog2'),
]
