import sys


def txt_importer(path_file):
    ext = path_file.split('.')[1]
    if (ext != 'txt'):
        return print('Formato inválido', file=sys.stderr)
    try:
        with open(path_file) as file:
            lines = list()
            for line in file.readlines():
                lines.append(line.replace('\n', ''))
            return lines
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
