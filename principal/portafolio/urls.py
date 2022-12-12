from django.urls import path
from .views import ProyectoList


urlpatterns = [
    path('mi-portafolio',ProyectoList.as_view(), name='portafolio')
]
