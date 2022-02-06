import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            return sys.stderr.write('Formato inválido\n')
        return open(path_file, "r").read().splitlines()
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
