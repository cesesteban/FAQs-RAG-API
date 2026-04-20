import os
import shutil
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from app.core.config import settings
from app.services.vertex_service import get_embeddings

def run_indexing(data_dir: str = "app/data"):
    """
    Refreshes the knowledge base by loading all files in the data directory.
    """
    print(f"Refreshing knowledge base from {data_dir}...")
    
    # 1. Clear existing index to avoid duplicates on refresh
    persist_directory = "chroma_data"
    if os.path.exists(persist_directory):
        print(f"Clearing existing index at {persist_directory}...")
        shutil.rmtree(persist_directory)
    
    # 2. Load all text documents from the directory
    if not os.path.exists(data_dir):
        print(f"Directory {data_dir} not found.")
        return

    loader = DirectoryLoader(data_dir, glob="**/*.txt", loader_cls=TextLoader)
    documents = loader.load()
    
    if not documents:
        print(f"No documents found in {data_dir}. Skipping indexing.")
        return

    # 3. Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=40
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Generated {len(chunks)} chunks from {len(documents)} files.")
    
    # 4. Initialize Embeddings & Compute
    embeddings = get_embeddings()
    if not embeddings:
        print("ERROR: Vertex AI project information not set. Indexing cannot proceed.")
        return

    # 5. Create new persistent index
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    print(f"Knowledge base successfully updated with {len(chunks)} chunks.")

if __name__ == "__main__":
    run_indexing()
