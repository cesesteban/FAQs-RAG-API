import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI
from app.services.indexer import run_indexing

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Start up: Initialize RAG engine, DB connections, etc.
    print(f"Starting up {app.title}...")
    
    # Force Automatic Re-indexing to always reflect current data files
    print("Refreshing knowledge base automatically from files...")
    try:
        run_indexing()
    except Exception as e:
        print(f"Warning: Automatic re-indexing failed: {e}")
    
    yield
    
    # Shut down: Clean up resources
    print(f"Shutting down {app.title}...")
