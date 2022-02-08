import sys
from os.path import exists


def txt_importer(path_file):
    if (path_file[-3:] != 'txt'):
        print('Formato inválido', file=sys.stderr)

    if not exists(path_file):
        return print(f'Arquivo {path_file} não encontrado', file=sys.stderr)

    with open(path_file, mode='r') as arch:
        line = arch.read().splitlines()
        return line


# https://www.kite.com/python/
# answers/how-to-read-a-newline-delimited-text-file-in-python

# https://www.delftstack.com/pt/howto/python/python-print-to-stderr
