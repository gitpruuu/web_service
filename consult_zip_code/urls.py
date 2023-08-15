from django.urls import path
from .views import consulta_cep

urlpatterns = [
    path('consulta-cep/<str:cep>/', consulta_cep, name='consulta-cep'),
]
