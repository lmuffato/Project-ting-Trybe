import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        return sys.stderr.write("Formato inválido\n")
    with open(path_file, "r") as file:
        return list(file.read().splitlines())
