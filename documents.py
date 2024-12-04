from collections import Counter
from dataclasses import dataclass

from analysis import analyze


@dataclass
class Document:
    ID: int
    title: str
    abstract: str
    url: str

    def analyze(self):
        self.term_frequencies = Counter(analyze(self.fulltext))

    def term_frequency(self, term):
        return self.term_frequencies.get(term, 0)

    @property
    def fulltext(self):
        return " ".join([self.title, self.abstract])
