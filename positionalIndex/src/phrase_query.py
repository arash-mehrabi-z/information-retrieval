from handle import parse_text

def get_index_values_of(index, tokens):
    result = []
    for token in tokens:
        if token in index:
            result.append(index.get(token).get())
    return result

def get_word_tokens(tokens):
    return [tokens[0], tokens[2]]

def get_query(index):
    content = input("Please enter your phrase query:\n")
    tokens = parse_text(content)
    k = 1
    if len(tokens) > 2:
        word_tokens = get_word_tokens(tokens)
        indices = get_index_values_of(index, word_tokens)
        k = tokens[1]
    else:
        indices = get_index_values_of(index, tokens)

    return indices, k
    