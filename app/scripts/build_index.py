import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.indexer import run_indexing

if __name__ == "__main__":
    run_indexing()
