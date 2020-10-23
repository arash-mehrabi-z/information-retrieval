from document import Document
from postingList import PostingList


class InvertedIndex():
    table = dict() # String, PostingList

    def add(self, document):
        tokens = document.getBody().split()
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

# doc1 = Document("one", "Hi I am a student in Urmia Univ. I student am .")
# doc2 = Document("two", "Hi I am Z. A student in student in Urmia Univ. I student am .")
# index = InvertedIndex()
# index.add(doc1)
# index.add(doc2)
# print(index.get("Salam"))
# print(index.table)