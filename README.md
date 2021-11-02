# Im-veis
O Sistema de Gerenciamento de imóveis foi feito no sistema operacionar windows. Esse tutorial de instalação será baseado no windows.

### Primeiro Passo
 Partindo da premissa que já esteja com python 3 instalado, vamos instalar o virtualen. Abra o Prompt de comando e digite:
 
 >>> pip install virtualenv

Logo  após  vamos criar o diretório do projeto:

>>> mkdir Imoveis
>>> cd Imoveis

Dentro do diretório do projeto  vamos criar o ambiente virtual:

>>> pip3 install -U pip virtualenv
>>> virtualenv --system-site-packages -p python3 ./venvimoveis
>>> .\venvimoveis\Scripts\activate

Com a máquina virtual ativada vamos instalar o Django.

>>> pip install django

Logo após vamos baixar o repositório do projeto que está aqui no github;

>>> git init 
>>>  git clone 'https://github.com/jopedrosilva/Im-veis.git'

Depois entre na pasta imoveis:

>>> cd imoveis

Agora, vamos executar o projeto:

>>> python ./manage.py runserver

Crie um usuário com o seu primeiro nome no username, e depois faça login no sistema. Dentro do sistema cadastre clientes antes de cadastrar vendas.
