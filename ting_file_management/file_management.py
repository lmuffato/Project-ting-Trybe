import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        print('Formato inválido', file=sys.stderr)
    try:
        with open(path_file, 'r', encoding='utf8') as file:
            content = file.readlines()
            return [line.rstrip('\n') for line in content]
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
