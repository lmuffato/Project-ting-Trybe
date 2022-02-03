import sys
from os.path import exists


# Referência: Imprimir para stderr em Python
# https://www.delftstack.com/pt/howto/python/python-print-to-stderr

# Referência: Checar se o arquivo existe
# https://www.pythontutorial.net/python-basics/python-check-if-file-exists

# cornflakes (E712) não permite: "if (exists(path_file) == False):"
# cornflakes prefere: "if not exists(path_file):"
# Porém ambas as opções passam no teste!

def txt_importer(path_file):
    if (path_file[-3:] != 'txt'):
        print('Formato inválido', file=sys.stderr)
    if not exists(path_file):
        print('Arquivo {} não encontrado'.format(path_file), file=sys.stderr)
