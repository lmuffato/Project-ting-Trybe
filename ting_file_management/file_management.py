import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return sys.stderr.write('Formato inválido\n')

    try:
        txt_file = open(path_file, "r").read().splitlines()
        return txt_file
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
