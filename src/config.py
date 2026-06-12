from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).parent.parent

# Data Paths
DATA_DIR = PROJECT_ROOT / "data"
RAW_DOCS_DIR = DATA_DIR / "raw_docs"
PROCESSED_DIR = DATA_DIR / "processed"

# Vector Store
VECTORSTORE_DIR = PROJECT_ROOT / "vectorstore"

# Chunking Settings
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150

# Retrieval Settings
TOP_K = 5