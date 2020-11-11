import xml.etree.ElementTree as ET
import preprocess
import stopword

def read_file(file_address):
    with open(file_address, 'r', encoding = 'utf-8') as f:
        file_content = f.read()

    return file_content

def is_xml():
    return True

def normalize(abstract):
    preprocessed = preprocess.PreProcess(abstract)
    preprocessed.normalize_letter()
    preprocessed.remove_punctuation()
    return preprocessed

def tokenize(normalized):
    tokens = normalized.tokenize()
    return tokens

def remove_stopwords(tokens):
    sword = stopword.StopWord()
    return sword.remove_stopwords(tokens)

def tokens_is_not_empty(tokens):
    return tokens

def parse_xml(file_content):
    root = ET.fromstring(file_content)
    for child in root:
        abstract = child.find('abstract').text
        normalized = normalize(abstract)
        tokens = tokenize(normalized)
        if tokens_is_not_empty(tokens):
            tokens = remove_stopwords(tokens)

if __name__ == '__main__':
    file_address = "/home/arash/learning/information_retrieval/assignment/ir/persianPreProcess/data/simple_small.xml"

    file_content = read_file(file_address)
    if(is_xml()):
        parse_xml(file_content)






