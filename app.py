import requests
import streamlit as st

def buscar_letra(banda, musica):
    endpoint =f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(endpoint)
    letra = response.json()["lyrics"] if response.status_code == 200 else "" 
    return letra


def salvar_sugestao(sugestao):
    with open("sugestoes.txt", "a") as f:
        f.write(sugestao + "\n")

    
st.image("robo_dancante.webp", caption = "Robo ouvindo musica", use_column_width=True)
st.title("A letra da sua musica!")


st.info("Desenvolvido por Danilo Nantes")


banda = st.text_input("Digite o nome da banda: ", key="banda")
musica = st.text_input("Digite o nome da musica: ", key= "musica")
pesquisar = st.button("Pesquisar")
sugestao = st.text_input("você tem alguma sugestão?")
Enviar = st.button("Enviar")

if pesquisar:
    letra = buscar_letra(banda, musica)
    if letra:
        st.success("Viva! Encontramos a letra da musica: ")
        st.text(letra)
    else:
        st.error("infelizmente não foi possivel encontrar a letra desejada")
if Enviar and sugestao:
    salvar_sugestao(sugestao)
    st.success("Obrigado pela sugestão!")

    
