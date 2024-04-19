from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('relatorio_geral/', relatorio_geral, name='relatorio_geral')
]
