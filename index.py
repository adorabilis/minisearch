import math

from analysis import analyze


class Index:
    """Represents an index of documents."""

    def __init__(self):
        self.index = {}
        self.documents = {}

    def index_document(self, document):
        """Adds a document to the index."""
        if document.ID not in self.documents:
            self.documents[document.ID] = document
            document.analyze()

        for token in analyze(document.fulltext):
            if token not in self.index:
                self.index[token] = set()
            self.index[token].add(document.ID)

    def document_frequency(self, token):
        """Returns the number of documents containing a token."""
        return len(self.index.get(token, set()))

    def inverse_document_frequency(self, token):
        """Returns the inverse document frequency of a token."""
        return math.log10(len(self.documents) / self.document_frequency(token))

    def search(self, query, search_type="AND", rank=True):
        """Searches the index for documents matching a query."""
        analyzed_query = analyze(query)
        results = self._results(analyzed_query)
        documents = [self.documents[doc_id] for doc_id in set.intersection(*results)]
        if rank:
            return self.rank(analyzed_query, documents)
        return documents

    def _results(self, analyzed_query):
        """Returns the sets of documents matching each query term."""
        return [self.index.get(token, set()) for token in analyzed_query]

    def rank(self, analyzed_query, documents):
        """Ranks documents by relevance to a query."""
        results = []
        for document in documents:
            score = 0.0
            for token in analyzed_query:
                tf = document.term_frequency(token)
                idf = self.inverse_document_frequency(token)
                score += tf * idf
            results.append((document, score))
        return sorted(results, key=lambda doc: doc[1], reverse=True)
