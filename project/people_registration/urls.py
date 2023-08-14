from django.urls import path
from people_registration.views import *

urlpatterns = [
    path('cadastrar-pessoa/', cadastrar_pessoa, name='cadastrar-pessoa'),
    path('listar-pessoas/', listar_pessoas, name='listar-pessoas'),
    path('listar-pessoa/<str:pessoa_id>', listar_pessoa, name='listar-pessoas'),
    path('editar-pessoa/<str:pessoa_id>', atualizar_pessoa, name='listar-pessoas'),
    path('excluir-pessoa/<str:pessoa_id>', excluir_pessoa, name='listar-pessoas'),
]