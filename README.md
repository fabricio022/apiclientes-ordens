# API de Cadastro de Clientes e Ordens de Serviço

Este projeto é uma API desenvolvida em **Django + Django REST Framework** para gerenciar **clientes** e **ordens de serviço (OS)**.  
Foi criado com foco em aprendizado e demonstração de CRUD (Create, Read, Update, Delete) e boas práticas de organização de projeto.

---

## 🚀 Funcionalidades
- 📌 Cadastro, listagem, atualização e exclusão de clientes
- 📌 Cadastro, listagem, atualização e exclusão de ordens de serviço
- 🔗 Relacionamento entre clientes e ordens de serviço
- 🛡️ Validações e tratamento de erros

---

## 🗂 Estrutura de Pastas
📂 projeto_api/
├── 📂 api_clientes/ # Aplicativo responsável pelos clientes
│ ├── models.py # Estrutura do banco (tabelas)
│ ├── serializers.py # Converte dados para JSON e valida
│ ├── views.py # Lógica das requisições HTTP
│ ├── urls.py # Rotas da API de clientes
│ └── tests.py # Testes automatizados
│
├── 📂 api_os/ # Aplicativo responsável pelas ordens de serviço
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── tests.py
│
├── 📂 projeto_api/ # Configurações principais do Django
│ ├── settings.py # Configurações globais
│ ├── urls.py # Rotas principais do projeto
│ └── wsgi.py # Interface de comunicação com servidor
│
├── manage.py # Comando para gerenciar o projeto
├── requirements.txt # Lista de dependências
└── .gitignore # Arquivos que não serão enviados ao GitHub
