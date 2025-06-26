from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from modules.load_vectorstore import load_vectorstore
from modules.llm import get_llm_chain
from modules.query_handlers import query_chain
from logger import logger


app = FastAPI(title="RagBot")

#allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend's URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def catch_exception_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        
@app.post("/upload_pdfs/")
async def upload_files(files: List[UploadFile] = File(...)):
    try:
        logger.info("Received files for upload")
        vectorstore = load_vectorstore(files)
        app.vectorstore = vectorstore  # 🔥 Save it in app state!
        logger.info("Vectorstore created successfully")
        return {"message": "PDFs uploaded and vectorstore ready!"}
    except Exception as e:
        logger.error(f"Error loading vectorstore: {e}")
        return JSONResponse(status_code=500, content={"message": "Error processing files"})
@app.post("/ask/")
async def ask_question(user_input: str = Form(...)):
    try:
        logger.info(f"Received question: {user_input}")
        if not hasattr(app, 'vectorstore'):
            return JSONResponse(status_code=400, content={"message": "No vectorstore available. Please upload PDFs first."})
        
        from langchain.vectorstores import Chroma
        from langchain.embeddings import HuggingFaceEmbeddings  

        vectorstore=Chroma(
            persist_directory="./chroma_store",
            embedding_function=HuggingFaceEmbeddings(model_name="all-MiniLM-L12-v2"),
        )
        chain=get_llm_chain(vectorstore)
        result= query_chain(chain, user_input)
        logger.info("Query processed successfully") 
        return result
    except Exception as e:
        logger.error(f"Error processing question: {e}")
        return JSONResponse(status_code=500, content={"message": "Error processing question"})

@app.get("/test") 
async def test():
    return {"message": "Hello, World!"}

