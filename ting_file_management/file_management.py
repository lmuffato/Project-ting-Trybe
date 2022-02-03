import sys


def txt_importer(path_file):
    if path_file.split('.')[1] != "txt":
        return sys.stderr.write("Formato inválido\n")

    try:
        file = open(path_file, mode="r")
        return file.read().split('\n')

    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
