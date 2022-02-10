import sys
from os.path import exists


def txt_importer(path_file):
    if (path_file[-3:] != 'txt'):
        print('Formato inválido', file=sys.stderr)

    if not exists(path_file):
        return print(f'Arquivo {path_file} não encontrado', file=sys.stderr)

    with open(path_file, mode='r') as file:
        file_row = file.read().splitlines()
        return file_row
