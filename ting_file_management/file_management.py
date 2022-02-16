import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file[-3:] == 'txt':
        return sys.stderr.write('Formato inválido\n')

    try:
        with open(path_file, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return sys.stderr.write(
            f"Arquivo {path_file} não encontrado\n"
            )
