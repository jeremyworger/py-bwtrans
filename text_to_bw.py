

def read_input_suffix_array(filename):
    with open(filename) as f:
        return map(int, f.readline().strip().split(' '))


def read_input_text(filename):
    with open(filename) as f:
        return f.readline().strip()


def construct_bw_transform(suffix_array, text):
    pass

