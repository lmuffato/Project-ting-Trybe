import sys
from os.path import exists


# Referência: Imprimir para stderr em Python
# https://www.delftstack.com/pt/howto/python/python-print-to-stderr

# Referência: Checar se o arquivo existe
# https://www.pythontutorial.net/python-basics/python-check-if-file-exists

# cornflakes (E712) não permite: "if (exists(path_file) == False):"
# cornflakes prefere: "if not exists(path_file):"
# Porém ambas as opções passam no teste!

# Referência: Como usar o .splitline()
# https://www.kite.com/python/answers/
# how-to-read-a-newline-delimited-text-file-in-python

def txt_importer(path_file):
    if not exists(path_file):
        return print(f'Arquivo {path_file} não encontrado', file=sys.stderr)

    if (path_file[-3:] != 'txt'):
        print('Formato inválido', file=sys.stderr)

    with open(path_file, mode='r') as arquivo_txt:
        linhas = arquivo_txt.read().splitlines()
        return linhas
