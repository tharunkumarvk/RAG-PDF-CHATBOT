# RAG PDF Chatbot

Ask questions about your PDFs and get grounded, citation-backed answers.  
Fast ingestion → smart chunking → semantic retrieval → LLM answer with sources.

## ✨ Features
- Multi-PDF upload & parsing
- Embeddings + vector search (FAISS / Chroma-ready)
- Citations (showing source/page)
- Pluggable LLM & embedding providers
- Lightweight API + optional Streamlit chat UI
- Guardrails to reduce hallucinations

## 🚀 Quick Start
```bash
git clone https://github.com/tharunkumarvk/RAG-PDF-CHATBOT
cd RAG-PDF-CHATBOT
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add your API keys
uvicorn src.api.main:app --reload
```
Query:
```bash
curl -X POST http://localhost:8000/query -H "Content-Type: application/json" \
  -d '{"question": "Summarize section 2", "top_k": 4}'
```

## 🧠 Stack
Python · FastAPI · (OpenAI or HuggingFace) · FAISS/Chroma · LangChain (optional) · Streamlit (UI)

## 🗂 Suggested Structure
```
src/
  ingestion/   # PDF load & clean
  processing/  # chunk + embed
  vectorstore/ # FAISS / Chroma adapters
  retrieval/   # similarity + filtering
  generation/  # LLM + answer builder
  api/         # FastAPI endpoints
  ui/          # Streamlit chat
```

## ⚙️ Env (.env)
```
OPENAI_API_KEY=...
EMBEDDING_PROVIDER=openai
VECTOR_STORE=faiss
CHUNK_SIZE=1000
TOP_K=5
```

## 🛣 Roadmap (Next)
- Hybrid (BM25 + vectors)
- Streaming replies
- Conversation memory
- Table / figure awareness
- RAG evaluation dashboard

## 🤝 Contribute
Fork → branch → PR.  
Keep code typed & formatted. Ideas welcome!

## 📜 License
MIT

---

Built for learning & experimentation. Always verify critical answers with the original document.
