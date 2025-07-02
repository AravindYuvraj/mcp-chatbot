# MCP Q&A Chatbot

An intelligent chatbot that answers questions about Model Context Protocol (MCP) concepts, implementation, best practices, and troubleshooting. Designed for developers and teams learning about MCP.

---

## 🚀 Features
- **Expert Q&A:** Ask anything about MCP (servers, clients, code, troubleshooting)
- **Code Examples:** Get ready-to-use MCP server/client code
- **Troubleshooting:** Solutions for common MCP issues
- **Simple Chat UI:** Developer-friendly interface using Streamlit
- **Customizable Knowledge Base:** Easily add or update MCP knowledge

---

## 📁 Project Structure
```
qa_chatbot/
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── mcp_knowledge/          # Knowledge base (Markdown files)
│   ├── concepts.md
│   ├── implementation.md
│   ├── troubleshooting.md
│   └── examples.md
└── README.md
```

---

## 🛠️ Setup Instructions
1. **Clone or download this repository.**
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set your OpenAI API key:**
   - The app will use the key from your environment or you can hardcode it in `app.py` (not recommended for production).
   - Example (Windows):
     ```sh
     set OPENAI_API_KEY=sk-...
     ```
   - Example (Linux/macOS):
     ```sh
     export OPENAI_API_KEY=sk-...
     ```
4. **Run the chatbot:**
   ```sh
   streamlit run app.py
   ```

---

## 💬 Usage
- Open the Streamlit app in your browser (usually at http://localhost:8501).
- Type your MCP-related question in the chat box and press "Ask".
- The bot will answer using the knowledge base and OpenAI's language model.

**Example questions:**
- What is an MCP server?
- How do I implement an MCP client?
- Show me a code example for MCP.
- How do I troubleshoot connection errors in MCP?

---

## 📝 Customization
- **Expand the knowledge base:**
  - Edit or add Markdown files in `mcp_knowledge/` to include more MCP topics, code, or troubleshooting tips.
- **Change the UI or logic:**
  - Modify `app.py` to adjust the chat interface or how answers are generated.

---

## 📜 License
MIT 