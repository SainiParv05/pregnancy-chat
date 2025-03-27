import streamlit as st
import main

st.title("Kaya - Pregnancy Support Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask Kaya anything about pregnancy!"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display a placeholder while the AI is generating a response
    response_container = st.empty()
    
    # Generate response from the backend
    response = main.generate(prompt)
    
    # Display response immediately
    response_container.chat_message("assistant").markdown(response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
