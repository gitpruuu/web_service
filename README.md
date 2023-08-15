Web Services Project

Este é um projeto Django que implementa web services RESTful para consulta de CEP e cadastro de pessoas. O projeto inclui dois aplicativos: cep_lookup para consultar informações de CEP e person_registration para cadastrar e listar pessoas.

Configuração

Pré-requisitos

Certifique-se de ter o Docker instalado em sua máquina.

Instalação

1. Clone este repositório para a sua máquina:

   git clone https://github.com/gitpruuu/web_service.git
   cd tex_test

2. Crie um ambiente virtual e ative-o:
   comando para Linux: python3 -m venv venv
   
   Ative o ambiente virtual: source venv/bin/activate

3. Instale as dependências:

   pip install -r requirements.txt

Uso

1. Construa e inicie o ambiente Docker:
   No doretório raiz do projeto existe um arquivo chamado start.sh, basta executa lo
   ./start.sh

2. Acesse os endpoints:

   - Consultar CEP: http://127.0.0.1:8000/consulta-cep/CEP_AQUI/
   - Cadastrar Pessoa: http://127.0.0.1:8000/cadastrar-pessoa/
   - Listar Pessoas: http://127.0.0.1:8000/listar-pessoas/
   - Listar Pessoas: http://127.0.0.1:8000/editar-pessoa/(id_pessoa)
   - Listar Pessoas: http://127.0.0.1:8000/excluir-pessoa/(id_pessoa)


   Substitua CEP_AQUI pelo CEP real que deseja consultar.
   Substitua id_pessoa pelo id real que deseja alterar.

Notas
## Cadastrar Pessoa

Para cadastrar uma nova pessoa na base, você pode fazer uma solicitação POST para o seguinte endpoint:
   - Listar Pessoas: http://127.0.0.1:8000/cadastrar-pessoa/
   e enviar no corpo da requisição um objeto json contendo nome e idade: {"nome": "nome123", "idade": "12"}

- O projeto usa o Django REST framework para implementar os web services RESTful.
- Certifique-se de configurar corretamente o arquivo settings.py para as apps cep_lookup e person_registration.
- O projeto inclui um ambiente Docker para simplificar a configuração.

Autor

[Johnatan Souza]