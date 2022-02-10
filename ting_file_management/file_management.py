import sys
from os import path


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido\n")
    if not path.exists(path_file):
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    with open(path_file) as file:
        result = [line.rstrip("\n") for line in file.readlines()]
        for line in file.readlines():
            print(line)
        return result
