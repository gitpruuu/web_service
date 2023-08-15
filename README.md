Web Services Project

Este é um projeto Django que implementa web services RESTful para consulta de CEP e cadastro de pessoas. O projeto inclui dois aplicativos: cep_lookup para consultar informações de CEP e person_registration para cadastrar e listar pessoas.

Configuração

Pré-requisitos

Certifique-se de ter o Docker instalado em sua máquina.

Instalação

1. Clone este repositório para a sua máquina:
   
   git clone https://github.com/gitpruuu/web_service.git
   cd web_service

2. Crie um ambiente virtual e ative-o:

   Comando para sistema Linux:
   python3 -m venv venv
   source venv/bin/activate

   Comando para sistema Windows:
   virtualenv venv
   venv\Scripts\Activate

3. Instale as dependências:

   pip3 install -r requirements.txt

4. Execute o ambiente Docker:

   **Nota:** Para executar o ambiente Docker no Windows, siga as instruções abaixo para executar o script `start.sh`.

   - Instale o Git Bash ou o Cygwin (ambos têm suporte a scripts `.sh`).

   - Abra o Git Bash ou o terminal do Cygwin.

   - Navegue até a pasta do projeto onde está localizado o arquivo `start.sh`.

   - Execute o seguinte comando:

     ```
     ./start.sh
     ```

Uso

1. Acesse os endpoints:

   - Consultar CEP: [http://127.0.0.1:8000/consulta-cep/CEP_AQUI/](http://127.0.0.1:8000/consulta-cep/CEP_AQUI/) (método GET)
   - Cadastrar Pessoa: [http://127.0.0.1:8000/cadastrar-pessoa/](http://127.0.0.1:8000/cadastrar-pessoa/) (método POST)
   - Listar Pessoas: [http://127.0.0.1:8000/listar-pessoas/](http://127.0.0.1:8000/listar-pessoas/) (método GET)
   - Listar Pessoa: [http://127.0.0.1:8000/editar-pessoa/(id_pessoa)](http://127.0.0.1:8000/editar-pessoa/(id_pessoa)) (método GET)
   - Excluir Pessoa: [http://127.0.0.1:8000/excluir-pessoa/(id_pessoa)](http://127.0.0.1:8000/excluir-pessoa/(id_pessoa)) (método PUT)

   Substitua CEP_AQUI pelo CEP real que deseja consultar.
   Substitua id_pessoa pelo id real da pessoa que deseja consultar ou excluir.

   **Nota:**

      - Em caso de erro verifique se possui o mongodb instalado localmente e execute o comando: sudo systemctl start mongod.service

Notas

- Cadastrar Pessoa: Para cadastrar uma nova pessoa na base, você pode fazer uma solicitação POST para o seguinte endpoint:
   - Listar Pessoas: [http://127.0.0.1:8000/cadastrar-pessoa/](http://127.0.0.1:8000/cadastrar-pessoa/)
   e enviar no corpo da requisição um objeto JSON contendo nome e idade: {"nome": "nome123", "idade": "12"}

- O projeto usa o Django REST framework para implementar os web services RESTful.
- Certifique-se de configurar corretamente o arquivo settings.py para as apps cep_lookup e person_registration.
- O projeto inclui um ambiente Docker para simplificar a configuração.

Autor

[Johnatan Souza]
