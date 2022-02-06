import sys


def txt_importer(path_file):
    try:
        with open(path_file, 'r') as file:
            text_list = file.read().splitlines()
        return text_list
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
