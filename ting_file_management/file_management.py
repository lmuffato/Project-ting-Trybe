import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file, mode="r") as file:
            arq = file.read().splitlines()
            return arq
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
