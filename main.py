import streamlit as st
from mistralai import Mistral

def generate_response(user_input):
    api_key = st.secrets["aielolo"]  # Utilisez des guillemets autour de "aielolo"
    model = "mistral-large-latest"
    client = Mistral(api_key=api_key)  # Utilisez la variable api_key ici
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": user_input,
            },
        ]
    )
    return chat_response.choices[0].message.content  # N'oubliez pas de retourner la réponse
st.title("Chatbot de la street")
st.write("Bienvenue sur l'interface de la street. Posez-moi des questions !")
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("Vous :", key="input")
    submit_button = st.form_submit_button(label='Envoyer')
if submit_button and user_input:
    response = generate_response(user_input)
    # Ajouter l'entrée utilisateur et la réponse à l'historique
    st.session_state.chat_history.append(("Vous", user_input))
    st.session_state.chat_history.append(("Bot", response))
for sender, message in st.session_state.chat_history:
    if sender == "Vous":
        st.write(f"**{sender}:** {message}")
    else:
        st.write(f"*{sender}:* {message}")
        