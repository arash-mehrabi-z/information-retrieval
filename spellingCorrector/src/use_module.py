from handle import create_index
from handle import load_index
from spelling_corrector import SpellingCorrector
from handle import parse_text

def get_query():
    content = input("Please enter your phrase query:\n")
    tokens = parse_text(content)
    return tokens

def correct_spelling(tokens, spelling_corrector):
    result = []
    for token in tokens:
        result.append(spelling_corrector.correction(token))
    
    return result

def print_result(tokens, index):
    for token in tokens:
        print(index[token])

if __name__ == '__main__':
    # file_address = "/home/arash/learning/information_retrieval/assignment/ir/positionalIndex/data/simple.xml"
    # index = create_index(file_address)
    index_address = "/home/arash/learning/information_retrieval/assignment/ir/spellingCorrector/data/index.pkl"
    index = load_index(index_address)
    spelling_corrector = SpellingCorrector(index)

    tokens = get_query()
    corrected_tokens = correct_spelling(tokens, spelling_corrector)
    print(corrected_tokens)
    print_result(corrected_tokens, index)
    