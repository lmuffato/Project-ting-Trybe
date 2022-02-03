import os
import sys
import pathlib


def txt_importer(path_file):
    ext = pathlib.Path(path_file).suffix.lower()
    if ext not in [".txt"]:
        return sys.stderr.write("Formato inválido\n")

    if os.path.exists(path_file) is not True:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    txt = None

    with open(path_file) as op:
        txt = op.read()

    print(txt)

    return txt.split('\n')

# txt_importer('statics/arquivo_teste.txt')
