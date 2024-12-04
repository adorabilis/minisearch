import gzip
import time

from lxml import etree

from documents import Document


def load_documents():
    """Load Wikipedia abstracts from XML file."""
    print("Parsing XML...")
    start = time.time()

    with gzip.open("data/enwiki-latest-abstract16.xml.gz", "rb") as f:
        doc_id = 1
        for _, element in etree.iterparse(f, events=("end",), tag="doc"):
            title = element.findtext("./title")
            url = element.findtext("./url")
            abstract = element.findtext("./abstract")
            yield Document(ID=doc_id, title=title, url=url, abstract=abstract)
            doc_id += 1
            element.clear()

    end = time.time()
    print(f"Parsing XML took {end - start} seconds")
