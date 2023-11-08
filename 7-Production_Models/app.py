# Importando bibliotecas
import numpy as np
import pandas as pd
import streamlit as st
import joblib
from sklearn.cluster import KMeans

# Definindo configuração da página
st.set_page_config(
    page_title="Detecção de Cédulas Falsas",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Definindo título
st.title("Detecção de Cédulas Falsas")
st.write(
    "Bem-vindo ao aplicativo de detecção de cédulas falsas. Insira os valores das características da cédula e preveja sua autenticidade usando um modelo KMeans previamente treinado."
)


# Carregando o modelo treinado
def carregar_modelo():
    return joblib.load("modelo_treinado.pkl")


# Recebendo as características da cédula
def cedula():
    st.subheader("Insira as características da cédula:")
    feature1 = st.number_input(
        "Comprimento da cédula (0-200):", min_value=0, max_value=200
    )
    feature2 = st.number_input(
        "Margem inferior da cédula (0-20):", min_value=0, max_value=20
    )
    return feature1, feature2


def predicao(modelo, feature1, feature2):
    user_data = pd.DataFrame(
        {
            "diagonal": [0],
            "height_left": [0],
            "height_right": [0],
            "margin_low": [feature2],
            "margin_up": [0],
            "length": [feature1],
        }
    )
    prediction = modelo.predict(user_data)
    return prediction[0]


# Retorna o resultado da predição
def resultado(predicao):
    st.subheader("Resultado")
    if predicao == 0:
        st.success("A cédula é verdadeira. 👍")
    else:
        st.error("A cédula é falsa. 👎")


if __name__ == "__main__":
    modelo = carregar_modelo()

    feature1, feature2 = cedula()

    # Botão para realizar a previsão
    if st.button("Prever"):
        predicao = predicao(modelo, feature1, feature2)
        resultado(predicao)
