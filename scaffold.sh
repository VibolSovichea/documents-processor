#!/bin/bash
set -e

mkdir -p app/{api/v1/routes,core,services/ocr,schemas,utils}
mkdir -p tests/
touch app/{__init__.py,main.py}
touch app/api/{__init__.py,dependencies.py}
touch app/api/v1/{__init__.py}
touch app/core/{__init__.py,config.py,logging_config.py,constants.py}
touch app/schemas/{__init__.py,upload.py,query.py}
touch app/utils/{__init__.py,downloader.py,text_utils.py}
touch app/services/{__init__.py,embeddings.py,vectorstore.py,document_pipeline.py,query_service.py}
touch app/services/ocr/{__init__.py,gemini_ocr.py,dots_ocr.py}
touch app/api/v1/routes/{upload.py,ocr.py,query.py}
touch tests/{__init__.py,test_upload.py,test_ocr.py,test_query.py}

# root files
cat > .env.example <<EOF
OPENAI_API_KEY=
GEMINI_API_KEY=
DOTS_OCR_API_KEY=
VECTOR_DB=pinecone
PINECONE_API_KEY=
PINECONE_ENVIRONMENT=
PINECONE_INDEX=document-index
EMBEDDING_MODEL=text-embedding-3-large
ENV=development
EOF

cat > requirements.txt <<EOF
fastapi
uvicorn
langchain
langchain-pinecone
langchain-openai
pydantic
requests
python-dotenv
httpx
tqdm
EOF

cat > README.md <<EOF
# FastAPI Document Processor

A modular document processing microservice using FastAPI, Gemini/DotOCR, and LangChain + Pinecone.

## Features
- OCR (Gemini / DotOCR)
- Khmer + English support
- Context embedding with LangChain
- Pinecone vector store
- URL-based uploads (S3 / Google Drive)
EOF

echo "✅ Project scaffolded successfully!"
