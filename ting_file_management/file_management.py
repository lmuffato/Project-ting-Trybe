import sys


def txt_importer(path_file):
    if 'txt' in path_file:
        try:
            data = open(path_file, 'r')
            content_list = []
            for i in data:
                content_list.append(i.rstrip('\n'))
            return content_list
        except FileNotFoundError:
            print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
    else:
        print('Formato inválido', file=sys.stderr)
