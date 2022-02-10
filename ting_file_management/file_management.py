import sys

accepted_file_type = ".txt"


def txt_importer(path_file):
    if accepted_file_type not in path_file:
        return sys.stderr.write("Formato inválido\n")
    try:
        return open(path_file, mode="r").read().splitlines()

    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
