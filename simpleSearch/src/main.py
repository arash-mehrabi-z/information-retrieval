books = dict()
names = ["alice", "beowulf", "frankenstein", "pride", "yellow"]

for name in names:
    with open("resource/text/" + name + ".txt") as f:
        text = f.read().lower()
        books[name] = text

while(True):
    inp = input("Please enter your query: ").lower()
    if inp == "quit":
        break

    for book in books:
        if inp in books[book]:
            print("Match: {}".format(book))
    