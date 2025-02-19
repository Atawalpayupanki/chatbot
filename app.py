import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

load_dotenv()
st.session_state.API_KEY=os.getenv("GOOGLE_API_KEY")
st.title("Hola")
st.markdown("bienvenido a 🤖chat")


prompt_template = PromptTemplate(
    input_variables=["history", "user_input"],
    template="Historial de la conversación:\n{history}\n\nUsuario: {user_input}\n\nAsistente:",
)


# with st.chat_message("assistant", avatar="🤖"):
#     st.write("Hola, soy un sigma")
# with st.chat_message("user", avatar="🌯"):
#     st.write("Hola")
st.session_state.geminai = ChatGoogleGenerativeAI(model="gemini-1.5-pro", api_key=st.session_state.API_KEY)

def generar_respuesta(mensage):
    st.write(mensage)
    return st.session_state.geminai.invoke(mensage)

if "mensages" not in st.session_state:
    st.session_state.mensages=[
        {"role": "assistant", "avatar": "🤖", "content": "hola, soy un sigma"}
    ]

mensage_usuario=st.chat_input("escribe aquí tu mensage")


for mensage in st.session_state.mensages:
    with st.chat_message(mensage["role"], avatar=(mensage["avatar"])):
        st.write(mensage["content"])

if mensage_usuario is not None:
    st.session_state.mensages.append(
        {"role": "user", "content": mensage_usuario, "avatar": "🌯"}
    )
    for mensage in st.session_state.mensages:
        historial=""
        historial=historial+f" {mensage["role"]}: {mensage["content"]} \n"

    
    prompt=prompt_template.format(
        history=historial,
        user_input=mensage_usuario
    )
    r=generar_respuesta(prompt).content
    with st.chat_message("user", avatar="🌯"):
        st.write(mensage_usuario)
    with st.chat_message("assistant", avatar="🤖"):
        st.write(r)
    st.session_state.mensages.append({"role": "assistant", "avatar": "🤖", "content": r})
