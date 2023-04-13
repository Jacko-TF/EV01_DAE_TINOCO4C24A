from django.urls import path

from . import views

app_name = 'pago'

urlpatterns = [

    path('', views.login, name='login'),
    path('loguear', views.loguear, name='loguear'),
    path('enviar', views.enviar, name='enviar')
]