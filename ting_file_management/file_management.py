import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        # Fonte: https://docs.python.org/3/library/sys.html
        # deve ser exibida uma mensagem: Formato inválido
        sys.stderr.write('Formato inválido\n')

    try:
        # read
        with open(path_file, 'r') as data:
            return data.read().split('\n')

    except FileNotFoundError:
        #  deve ser exibida a mensagem: Arquivo {path_file} não encontrado
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
