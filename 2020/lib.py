def get_input(path: str, split_by: str):
    file = open(path, 'r')
    return file.read().split(split_by)


def get_raw_input(path: str):
    file = open(path, 'r')
    return file.read()
