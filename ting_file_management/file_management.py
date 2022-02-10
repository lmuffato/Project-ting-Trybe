import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    try:
        if not str(path_file).endswith(".txt"):
            return print("Formato inválido", file=sys.stderr)
        with open(path_file) as file:
            return file.read().splitlines()

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
