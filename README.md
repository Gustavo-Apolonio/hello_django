- [Hello Django](#hello-django)
- [Tutorial](#tutorial)
  * [Ambiente](#ambiente)
  * [Iniciando](#iniciando)
  * [No PyCharm:](#no-pycharm-)
      - [Configs de ambiente](#configs-de-ambiente)
      - [Iniciando server](#iniciando-server)
  * [Django App](#django-app)
  * [Adicionando Rotas ao App](#adicionando-rotas-ao-app)
- [Desafios](#desafios)
    + [1. Entenda parâmetros no _Django_](#1-entenda-par-metros-no--django-)
    + [2. Rota de soma:](#2-rota-de-soma-)
    + [3. No mesmo esquema da rota de cima, criar uma rota para multiplicar, dividir e subtrair!](#3-no-mesmo-esquema-da-rota-de-cima--criar-uma-rota-para-multiplicar--dividir-e-subtrair-)
    + [Respostas](#respostas)

# Hello Django

_Just a hello world with django._



# Tutorial



## Ambiente

* _OS_: Linux
* _Python_: 3.8
* _PyCharm_: Community
* _Local do Projeto_: /home/user/Projeto/hello_django

---

## Iniciando

1. Entrar na pasta das _virtualenvs_ :

``` bash	
/home/user~$ cd .virtualenvs
```

> Caso não exista, crie a pasta .virtualenv

2. Criar a _virtualenv_ :

``` bash
/home/user/.virtualenv~$ sudo apt-get install python3-pip
/home/user/.virtualenv~$ sudo pip3 install virtualenv
/home/user/.virtualenv~$ virtualenv -p /usr/bin/python3.8 dev_django
```

> Confira _[virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)_ para entender melhor.

3. Entrar na pasta da _virtualenv_ :

```bash
/home/user/.virtualenv~$ cd dev_django
/home/user/.virtualenv/dev_django~$ source bin/activate
```

4. Atualizar o _pip_ e instalar o _django_ :

```bash
(dev_django) /home/user/.virtualenv/dev_django~$ python -m pip install --upgrade pip
(dev_django) /home/user/.virtualenv/dev_django~$ pip install django
```

5. Entrar na pasta do projeto e iniciar o _django_ :

   ```bash
   (dev_django) /home/user/.virtualenv/dev-django~$ cd /home/user/Projeto/
   (dev_django) /home/user/Projeto~$ django-admin startproject hello_django
   ```

---

## No PyCharm:

#### Configs de ambiente

1. Abra a pasta do projeto

2. Vá nas configurações - pesquise por interpreter

3. Em _Python Interpreter_ selecione _Show All_ 

4. Adicione um ambiente virtual novo - clique em  **+**

5. Existing environment

   1. Interpreter

   2. Clique nos **...** para buscar o ambiente virtual

   3. Procure pelo ambiente virtual criado no passo 2 e 3

   4. Selecione o interpretador python dentro da pasta bin:

      ```bash
      /home/apolonio/.virtualenvs/dev_django/bin/python
      ```

   5. Clique em OK ; OK ; Apply & OK

#### Iniciando server

1. No explorador a esquerda, clique duas vezes sobre o manage.py
2. Clique com o botão direito sobre o arquivo 
3. Modify run configuration...
   * Parameters - coloque _runserver_
4. Run (Ctrl + F10)
5. Abra no seu [localhost](http://127.0.0.1:8000)

> PARABÉNS, TEU SERVER ESTÁ OFICIALMENTE RODANDO LOCALMENTE!

---

## Django App

**_AINDA NO PYCHARM_**

Abra o _terminal_ - verifique que estará com o _virtualenv_ ativo :

1. Vamos iniciar o app através do _core_ :

   ```bash	
   (dev_django) /home/user/Projeto/hello_django~$ django-admin startapp core
   ```

2. Isso criará uma pasta chamada _core_ - sabendo disso vamos abrir nosso _```~/hello_django/settings.py```_ :

   Localize a variável de ```INSTALLED_APPS``` e vamos alterar para :

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'core' # estamos adicionando o app ** core **
   ]
   ```

   A cada app adicionado, temos que adicionar à esta variável

## Adicionando Rotas ao App

Em _```~/hello_django/urls.py```_ adicione o ```path('hello/', views.hello)``` que ficará assim:

```python
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello)
]
```

Para configurar o views, vamos abrí-lo em _```~/core/views.py```_ e adicionar nossa função para retornar o querido ```'Hello World!'``` no nosso site/server

```python
from django.shortcuts import render, HttpResponse 
									# importe o HttpResponse
    								# para retornar como HTML no site/server

# Create your views here.

def hello(req):
    return HttpResponse(f'<h1>Hello World!</h1>')
```

---

# Desafios

### 1. Entenda parâmetros no _Django_

> Dica: 
>
> ```python
> ~/core/views.py
> 
> def hello(req, param1, param2, paramN):
>     return HttpResponse(f'<h1>Hello {param1}! I`m {param2} <br /> I have {paramN} params</h1>')
> 
> ~/hello_django/settings.py
> 
> urlpatterns = [
>     path('admin/', admin.site.urls),
>     path('hello/<param1>?param2=<param2>/<int:paramN>', views.hello)
> ]
> ```

### 2. Rota de soma:

> Parametros: ```<int:num1> & <int:num2>```
>
> Rota: ```/soma``` 
>
> Retorno: ```Soma de _num1_ com _num2_```

### 3. No mesmo esquema da rota de cima, criar uma rota para multiplicar, dividir e subtrair!

### Respostas

* [URLs](https://github.com/Gustavo-Apolonio/hello_django/blob/master/hello_django/urls.py)
* [Views](https://github.com/Gustavo-Apolonio/hello_django/blob/master/core/views.py)

---

---

###### Fonte: [Digital Innovation One](https://web.digitalinnovation.one/course/desenvolvimento-para-internet-e-banco-de-dados-com-python-e-django/learning/8084a070-3bcd-47c8-93d1-683880f3cd00?back=/browse)

