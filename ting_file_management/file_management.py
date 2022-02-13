import sys
from os.path import exists


def txt_importer(path_file):
    array_name = path_file.split(",")
    if (array_name[len(array_name) - 1] != 'txt'):
        print('Formato inválido', file=sys.stderr)
    if not exists(path_file):
        return print(f'Arquivo {path_file} não encontrado', file=sys.stderr)

    return open(path_file, mode="r").read().splitlines()
