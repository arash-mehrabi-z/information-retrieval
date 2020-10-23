from documentStore import DocumentStore
from invertedIndex import InvertedIndex
from document import Document


books = dict()
names = ["alice", "beowulf", "frankenstein", "pride", "yellow"]
docStore = DocumentStore()
index = InvertedIndex()

for name in names:
    with open("resource/text/" + name + ".txt") as f:
        body = f.read().lower()
        document = Document(name, body)
        docStore.add(document)
        index.add(document)
        
while(True):
    inp = input("Please enter your query: ").lower()
    if inp == "quit":
        break

    lst = index.getPostingList(inp)

    if lst != None:
        for docId in lst.getDocIds():
            print(docStore.getDoc(docId))
    else:
        print("No match found.")
    