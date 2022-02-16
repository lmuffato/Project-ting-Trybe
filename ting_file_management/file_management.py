import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith('.txt'):
            sys.stderr.write("Formato inválido\n")
            return None

        with open(path_file, mode='r') as file:
            return file.read().split('\n')

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
