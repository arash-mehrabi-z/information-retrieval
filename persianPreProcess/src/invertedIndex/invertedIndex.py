from .document import Document
from .postingList import PostingList


class InvertedIndex():
    table = dict() # String, PostingList

    def get_table(self):
        return self.table

    def get_posting_list(self, key):
        if key in self.table:
            return self.table[key]
        else:
            return None

    def add(self, document, tokens):
        distinctTokens = set(tokens)

        for token in distinctTokens:
            if not token in self.table:
                self.table[token] = PostingList([])
            self.table[token].add(document.getDocId())

    def getPostingList(self, token):
        if token in self.table:
            return self.table[token]  
        else:
            return None

    def __repr__(self) -> str:
        return self.table.__str__()
