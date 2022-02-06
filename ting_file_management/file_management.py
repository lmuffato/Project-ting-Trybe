import sys


def txt_importer(path_file):
    try:
        if path_file.endswith('.txt') is False:
            return sys.stderr.write('Formato inválido\n')
        else:
            with open(path_file, 'r') as file:
                text_list = file.read().splitlines()
            return text_list
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
