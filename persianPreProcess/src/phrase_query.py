from use_module import parse_text

def get_index_values_of(index, tokens):
    result = []
    for token in tokens:
        if token in index.getTable():
            result.append(index.get(token).get())
    return result


def get_query(index):
    content = input("Please enter your query:\n")
    tokens = parse_text(content)
    print(tokens)
    # indices = get_index_values_of(index, tokens)
    # return indices
    