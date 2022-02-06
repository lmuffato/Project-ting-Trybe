import sys


def txt_importer(path_file):
    # verificar se o arquivo termina com .txt
    if not path_file.endswith(".txt"):
        return sys.stderr.write('Formato inválido\n')
    try:
        file = open(path_file, "r")
        return file.read().split('\n')
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
