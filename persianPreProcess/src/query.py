from use_module import parse_text

class Query():
    def __init__(self, doc_store, index):
        self.doc_store = doc_store
        self.index = index

    def print_doc_ids(self, doc_ids):
        for doc_id in doc_ids:
            print(self.doc_store.getDoc(doc_id))

    def AND_doc_ids(self, p1, p2):
        result = p1.AND(p2)
        self.print_doc_ids(result.getDocIds())

    def OR_doc_ids(self, p1, p2):
        result = p1.OR(p2)
        self.print_doc_ids(result.getDocIds())

    def NOT_doc_ids(self, p1, p2):
        result = p1.NOT(p2)
        self.print_doc_ids(result.getDocIds())

    def choose_boolean_operator(self, tokens):
        p1 = self.index.get_posting_list(tokens[0])
        operator = tokens[1]
        p2 = self.index.get_posting_list(tokens[2])
        if operator == "AND":
            self.AND_doc_ids(p1, p2)
        elif operator == "OR":
            self.OR_doc_ids(p1, p2)
        elif operator == "NOT":
            self.NOT_doc_ids(p1, p2)
        else:
            print("Invalid query.")

    def biword_query(self, tokens):
        p1 = self.index.get_posting_list(tokens[0])
        p2 = self.index.get_posting_list(tokens[1])
        self.AND_doc_ids(p1, p2)

    def aword_query(self, tokens):
        p = self.index.get_posting_list(tokens[0])
        self.print_doc_ids(p.getDocIds())

    def get_query(self):
        content = input("Please enter your query:\n")
        tokens = parse_text(content)
        if len(tokens) == 3 :
            self.choose_boolean_operator(tokens)
        elif len(tokens) == 2:
            self.biword_query(tokens)
        elif len(tokens) == 1:
            self.aword_query(tokens)