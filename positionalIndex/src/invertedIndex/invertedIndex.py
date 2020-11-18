from invertedIndex.document import Document
from invertedIndex.postingList import PostingList


class InvertedIndex():
    table = dict() # String, PostingList

    def add(self, document, tokens):
        position = 0

        for token in tokens:
            if not token in self.table:
                self.table[token] = PostingList(token)
            self.table[token].add(document.getDocId(), position)
            position += 1

    def getPostingList(self, token):
        if token in self.table:
            return self.table[token]  
        else:
            return None

    def get(self, key):
        return self.table[key]

    def getTable(self):
        return self.table

    def __repr__(self) -> str:
        return self.table.__str__()

# doc1_body = "salam I am very good man am nice man"
# doc2_body = "hello you are a very good girl not a man man"
# doc1 = Document("first", doc1_body)
# doc2 = Document("second", doc2_body)
# index = InvertedIndex()
# index.add(doc1, doc1.getBody().split())
# index.add(doc2, doc2.getBody().split())
# print(index)