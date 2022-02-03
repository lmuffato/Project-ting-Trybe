import os.path
import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not os.path.isfile(path_file):
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido\n")

    with open(path_file) as file:
        response = file.read().splitlines()
        # https://www.tutorialspoint.com/python3/string_splitlines.htm
        return response
