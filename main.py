import os.path
import time

from index import Index
from load import load_documents


def main():
    """Runs the search engine."""
    index = Index()
    for document in load_documents():
        index.index_document(document)
    query = "artificial intelligence"
    results = index.search(query)
    for document, score in results:
        print(f"{document.title} - {score}")


if __name__ == "__main__":
    if not os.path.exists("data/enwiki-latest-abstract16.xml.gz"):
        raise FileNotFoundError("Data file not found")
    else:
        main()
