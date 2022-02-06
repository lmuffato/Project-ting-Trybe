import sys


def txt_importer(path_file):
    if path_file.endswith('.txt'):
        try:
            with open(path_file, 'r') as file:
                result = []
                for line in file.readlines():
                    result.append(line.replace('\n', ''))
                return result
        except FileNotFoundError:
            return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
    sys.stderr.write('Formato inválido\n')
