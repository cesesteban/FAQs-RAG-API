import asyncio
import json
import os
import sys
import argparse

# Add project root to sys.path
sys.path.append(os.getcwd())

from app.services.rag_engine import generate_rag_response
from app.schemas.rag import RAGQuery

async def query_main(question: str, lang: str):
    """
    Fulfills M2 requirement: script to run queries from command line.
    """
    payload = RAGQuery(query=question, lang=lang)
    try:
        response = await generate_rag_response(payload)
        # Print formatted JSON to stdout
        print(json.dumps(response.model_dump(), indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query the FAQ RAG API CLI")
    parser.add_argument("query", help="The question to ask")
    parser.add_argument("--lang", default="es", help="Language for the response (es/en)")
    
    args = parser.parse_args()
    asyncio.run(query_main(args.query, args.lang))
