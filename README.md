# 🎓 Este é o EdioHub!

O EdioHub é um sistema de organização de estudos desenvolvido em Python para a disciplina de **PISI1**.  
O objetivo do projeto é ajudar estudantes a integrar funcionalidades como: gerenciar disciplinas; registrar tempo de estudo; acompanhar estatísticas e organizar tarefas. O foco é incluir todas estas funcionalidades em uma única aplicação para evitar a dispersão de funcionalidades em diferentes serviços e servir como central de estudos e produtividade pessoal.

---

# 📌 Sobre o projeto

O **EdioHub** é um aplicativo em terminal que permite ao usuário:

- Criar conta e fazer login seguro
- Registrar disciplinas
- Controlar tempo de estudo
- Visualizar estatísticas de desempenho
- Criar e gerenciar tarefas

O foco do projeto é aplicar conceitos de:

- Programação em Python  
- Banco de dados SQLite  
- Organização de código em módulos  
- Segurança de senhas com hash  

---

# 🚀 Funcionalidades - 1VA

## 🔐 Sistema de usuários
- Cadastro de conta  
- Login com senha criptografada (bcrypt)

## 📚 Gerenciamento de estudos e Produtividade
- Cadastro de disciplinas  
- Registro de tempo estudado  
- Estatísticas por disciplina
- Sistema de to-do list  

# 🚀 Funcionalidades - 2VA (WIP e sujeitas a alteração)
- Criação de perfil pessoal
- Objetivos (metas)
- Caminhos (guia)
- Anexos
- Notificações internas

# 🚀 Funcionalidades - 3VA (WIP e sujeitas a alteração)
- Grupos com fóruns
- Amizades com streak em dupla
- Conquistas expostas no perfil
- Gavetas para organizar e guardar materiais e links
- Filtros de materiais favoritos

  
---

# 🛠️ Tecnologias e bibliotecas utilizadas

- Python 3.14.3
- SQLite3 para databse
- Bcrypt(não-padrão) para hashing de senhas
- Time para contagens
- Datetime para datas de tempo

---

# 📦 Como executar o projeto

```bash
# 1️⃣ Clonar o repositório
git clone https://github.com/luiandoliv-cpu/Edio-Hub.git

# 2️⃣ Entrar na pasta do projeto
cd Edio-Hub

# 3️⃣ Instalar dependências
pip install bcrypt

# 4️⃣ Executar o programa
python main.py
```

---

# 📁 Estrutura do projeto

```bash
Edio-Hub/
│
├── main.py              # Arquivo principal
├── accko.db             # Banco de dados SQLite
│
├── serv/                # Lógica do sistema
│   
├── screens/             # Prints do sistema
└── README.md
```

---

# 💻 Como usar

1. Execute o programa  
2. Crie uma conta  
3. Faça login  
4. Cadastre suas disciplinas  
5. Registre seu tempo de estudo  
6. Acompanhe suas estatísticas  
7. Gerencie suas tarefas 

---

# 🎯 Objetivo acadêmico

Projeto desenvolvido como atividade prática da disciplina **PISI1**, com foco em persistência de dados, organização de software e práticas de programação.

---

# 👨‍💻 Autor

Desenvolvido por **Paulo Andrey**  
GitHub: https://github.com/luiandoliv-cpu
Fluxogramas: https://drive.google.com/drive/u/1/folders/1DZnUJMzX-PRPePyKETu32PQV0rnlwSg2

---