import sys


def txt_importer(path_file):
    if path_file.endswith(".txt") is False:
        return sys.stderr.write("Formato inválido\n")

    try:
        with open(path_file) as file:
            arq = file.read()
    except FileNotFoundError:
        return sys.stderr.write(
            f"Arquivo {path_file} não encontrado\n"
        )
    else:
        return arq.split("\n")
