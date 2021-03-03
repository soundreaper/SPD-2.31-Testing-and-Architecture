# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/

def calculate_area_under_graph(graph):
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################


def get_max_value(arr):
    max_val = arr[0]

    for val in arr:
        if val > max_val:
            max_val = val

    return max_val


arr = [5, -1, 43, 32, 87, -100]
print(get_max_value(arr))

############################


def split_word_whitespace(sentence):
    return sentence[0:].split(' ')


print(split_word_whitespace('If you were a vegetable, you’d be a ‘cute-cumber.'))
