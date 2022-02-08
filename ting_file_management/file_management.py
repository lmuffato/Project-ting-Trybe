import sys
import os.path


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        return sys.stderr.write('Formato inválido\n')
    if not os.path.isfile(path_file):
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')

    list_file = open(path_file, 'r').read().splitlines()
    return list_file
