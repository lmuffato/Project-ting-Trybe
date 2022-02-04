import sys


def txt_importer(path_file):
    if not path_file.endswith('txt'):
        print('Formato inválido', file=sys.stderr)

    with open(path_file, 'r') as file:
        content = file.read()
        return content.split('\n')
