# os path source: https://pythonspot.com/read-file/
import os.path
import sys


def txt_importer(path_file):
    if os.path.isfile(path_file):
        if path_file.endswith('.txt'):
            with open(path_file) as file:
                content = file.read().splitlines()
                return content
        return sys.stderr.write("Formato inválido\n")
    return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
