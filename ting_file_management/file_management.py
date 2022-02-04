import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return sys.stderr.write('Formato inválido\n')
    data = open(path_file, "r")
    if(not data):
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')

    text = data.read().splitlines()
    return text
