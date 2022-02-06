import sys


def txt_importer(path_file):
    if path_file.endswith(".txt"):
        try:
            with open(path_file) as file:
                return file.read().splitlines()
        except FileNotFoundError:
            return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    return sys.stderr.write('Formato inválido\n')
