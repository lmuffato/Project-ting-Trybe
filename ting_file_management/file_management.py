import sys


def txt_importer(path_file):
    if 'txt' in path_file:
        try:
            data = open(path_file, 'r')
            content = []
            for line in data:
                content.append(line.rstrip('\n'))
            return content
        except FileNotFoundError:
            print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
    else:
        print('Formato inválido', file=sys.stderr)
