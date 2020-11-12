from invertedIndex.invertedIndex import InvertedIndex
from invertedIndex.document import Document
from invertedIndex.documentStore import DocumentStore
import xml.etree.ElementTree as ET
import preprocess
import stopword

doc_store = DocumentStore() 
index = InvertedIndex()

def read_file(file_address):
    with open(file_address, 'r', encoding = 'utf-8') as f:
        file_content = f.read()

    return file_content

def is_xml():
    return True

def normalize(text):
    preprocessed = preprocess.PreProcess(text)
    preprocessed.normalize_letter()
    preprocessed.remove_punctuation()
    return preprocessed

def tokenize(normalized):
    tokens = normalized.split()
    return remove_stopwords(tokens)

def remove_stopwords(tokens):
    sword = stopword.StopWord()
    return sword.remove_stopwords(tokens)

def tokens_is_not_empty(tokens):
    return tokens

def add_to_doc_store(document):
    global doc_store
    doc_store.add(document)

def get_normalized_title(doc):
    title = doc.find('title').text
    return normalize(title)

def get_normalized_abstract(doc):
    abstract = doc.find('abstract').text
    return normalize(abstract)

def create_doc(doc):
    normalized_title = get_normalized_title(doc)
    normalized_abstract = get_normalized_abstract(doc)
    document = Document(normalized_title.text, normalized_abstract.text)
    add_to_doc_store(document)
    return document

def add_to_inverted_index(document, tokens):
    global index
    index.add(document, tokens)

def write_index_to_file(index):
    f = open("persianPreProcess/data/index.txt", "w")
    f.write(str(index))
    f.close()

def parse_xml(file_content):
    import time
    start_time = time.time()
    root = ET.fromstring(file_content)
    for doc in root:
        document = create_doc(doc)
        tokens = tokenize(document.getBody())
        add_to_inverted_index(document, tokens)
        if document.getDocId() % 1500 == 0:
            print(document.getDocId(), time.time() - start_time)
    write_index_to_file(index)
        
if __name__ == '__main__':
    file_address = "/home/arash/learning/information_retrieval/assignment/ir/persianPreProcess/data/simple.xml"

    file_content = read_file(file_address)
    if(is_xml()):
        parse_xml(file_content)






