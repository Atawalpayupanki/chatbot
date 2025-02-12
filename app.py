import streamlit as st
st.title("Hola")
st.markdown("bienvenido a 🤖chat")
# with st.chat_message("assistant", avatar="🤖"):
#     st.write("Hola, soy un sigma")
# with st.chat_message("user", avatar="🌯"):
#     st.write("Hola")

if "mensages" not in st.session_state:
    st.session_state.mensages=[
        {"role": "assistant", "avatar": "🤖", "content": "hola, soy un sigma"}
    ]

mensage_usuario=st.chat_input("escribe aquí tu mensage")
if mensage_usuario is not None:
    st.session_state.mensages.append(
        {"role": "user", "content": mensage_usuario, "avatar": "🌯"}
    )
    # with st.chat_message("assistant", avatar="🤖"):
        # st.write(f"porque dices {mensage_usuario}")
    st.session_state.mensages.append({"role": "assistant", "avatar": "🤖", "content": f"porque dices {mensage_usuario}"})

for mensage in st.session_state.mensages:
    with st.chat_message(mensage["role"], avatar=(mensage["avatar"])):
        st.write(mensage["content"])