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

    
st.image("https://files.oaiusercontent.com/file-VT4dhdNg2qbAmwi6uUL2Rp?se=2025-02-07T02%3A07%3A37Z&sp=r&sv=2024-08-04&sr=b&rscc=max-age%3D604800%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3Dd2c3db1f-680e-4dba-b1b8-d3264b307269.webp&sig=BDmu8q1CnTM5OVQR2bRnvlTzgl3myxbs/k4CnjSYMeE%3D")

st.title("Letras de musicas")

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

    
