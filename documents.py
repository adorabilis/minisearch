from collections import Counter
from dataclasses import dataclass

from analysis import analyze


@dataclass
class Document:
    """Represents a document with ID, title, abstract, and URL."""

    ID: int
    title: str
    abstract: str
    url: str

    def analyze(self):
        """Analyzes the document's title and abstract."""
        self.term_frequencies = Counter(analyze(self.fulltext))

    def term_frequency(self, term):
        """Returns the frequency of a term in the document's field."""
        return self.term_frequencies.get(term, 0)

    @property
    def fulltext(self):
        """Returns the document's full text (title and abstract)."""
        return " ".join([self.title, self.abstract])
