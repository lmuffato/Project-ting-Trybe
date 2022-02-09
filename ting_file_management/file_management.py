from functools import lru_cache
import sys
import os.path

@lru_cache
def txt_importer(path_file):
    formatFile = os.path.splitext(path_file)[1]
    if(formatFile != '.txt'):
        return sys.stderr.write('Formato inválido\n')
    try:
        with open(path_file, 'r', encoding='utf8') as file:
            reader = file
            lisText = [rows.strip('\n') for rows in reader]
            return lisText
    except FileNotFoundError:
        return sys.stderr.write(
            'Arquivo {} não encontrado\n'
            .format(path_file))
