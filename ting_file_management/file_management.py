import sys


def txt_importer(path_file):
    # """Aqui irá sua implementação"""
    if path_file.endswith(".txt"):
        try:
            with open(path_file, mode="r") as file:
                return file.read().splitlines()
        except FileNotFoundError:
            sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    else:
        sys.stderr.write("Formato inválido\n")

# Ref. para printar mensagens de erro stderr:
# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python

# Ref. para quebrar linhas nos limites de cada string:
# https://www.geeksforgeeks.org/python-string-splitlines-method/
