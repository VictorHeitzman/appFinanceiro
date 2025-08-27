#!/bin/bash

# Nome do repositório remoto no GitHub
REPO_URL="https://github.com/VictorHeitzman/appFinanceiro.git"

# Inicializa o repositório Git
git init

# Adiciona os arquivos do projeto
git add app.py database.py usuarios.db

# Faz o primeiro commit
git commit -m "Primeiro commit do app Streamlit com SQLite"

# Adiciona o repositório remoto
git remote add origin $REPO_URL

# Sobe os arquivos para o GitHub (branch main)
git branch -M main
git push -u origin main
