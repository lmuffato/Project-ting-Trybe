import sys


def txt_importer(path_file):
    try:
        log = list()
        if path_file.endswith('.txt'):
            with open(path_file) as file:
                log = file.read().split('\n')
                return log
        else:
            print("Formato inválido", file=sys.stderr)
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
