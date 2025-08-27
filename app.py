
import streamlit as st
from database import Database

db = Database()

st.title("Tela de Login")

aba = st.sidebar.radio("Menu", ["Login", "Cadastro"])

if aba == "Login":
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if db.verificar_login(usuario, senha):
            st.success(f"Login bem-sucedido! Bem-vindo, {usuario}.")
        else:
            st.error("Usuário ou senha incorretos.")

elif aba == "Cadastro":
    novo_usuario = st.text_input("Novo usuário")
    nova_senha = st.text_input("Nova senha", type="password")

    if st.button("Cadastrar"):
        if db.adicionar_usuario(novo_usuario, nova_senha):
            st.success("Usuário cadastrado com sucesso!")
        else:
            st.error("Usuário já existe. Escolha outro nome.")
