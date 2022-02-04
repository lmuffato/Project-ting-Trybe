import sys


def txt_importer(path_file):
    if path_file.endswith(".txt") == False:
        return sys.stderr.write("Formato inválido\n")

    try:
        arq = open(path_file, "r")
    except FileNotFoundError:
        return sys.stderr.write(
            f"Arquivo {path_file} não encontrado\n"
        )
    else:
        arq = arq.read()
        return arq.split("\n")
