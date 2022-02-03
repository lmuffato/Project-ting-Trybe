import sys


def txt_importer(path_file):
    if 'txt' in path_file:
        data = open(path_file, 'r')
        content = []
        for line in data:
            content.append(line.rstrip('\n'))
        return content
    else:
        print('Formato inválido', file=sys.stderr)
