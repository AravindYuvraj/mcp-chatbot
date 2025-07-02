import streamlit as st
import openai
import os

# Load knowledge base files
KNOWLEDGE_DIR = 'mcp_knowledge'
def load_knowledge():
    knowledge = ''
    if os.path.isdir(KNOWLEDGE_DIR):
        for fname in os.listdir(KNOWLEDGE_DIR):
            with open(os.path.join(KNOWLEDGE_DIR, fname), 'r', encoding='utf-8') as f:
                knowledge += f.read() + '\n'
    return knowledge

# Set your OpenAI API key here or via environment variable
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI(api_key=OPENAI_API_KEY)

st.set_page_config(page_title="MCP Q&A Chatbot", page_icon="🤖")
st.title("🤖 MCP Q&A Chatbot")
st.write("Ask me anything about Model Context Protocol (MCP)!")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Your question:")

if st.button("Ask") and user_input:
    st.session_state.chat_history.append(("user", user_input))
    with st.spinner("Thinking..."):
        # Retrieve knowledge base
        kb = load_knowledge()
        # Compose prompt
        prompt = f"You are an expert on Model Context Protocol (MCP). Use the following knowledge base to answer the user's question.\n\nKnowledge Base:\n{kb}\n\nUser Question: {user_input}\n\nAnswer as an MCP expert, with clear explanations and code examples if relevant."
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert on Model Context Protocol (MCP)."},
                    {"role": "user", "content": prompt}
                ]
            )
            answer = response.choices[0].message.content
        except Exception as e:
            answer = f"Error: {e}"
        st.session_state.chat_history.append(("bot", answer))

# Display chat history
for role, msg in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**MCP Bot:** {msg}") 