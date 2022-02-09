import sys


def txt_importer(path_file):
    if path_file.endswith(".txt"):
        try:
            txt_file = open(path_file, "r")
            return txt_file.read().splitlines()
        except FileNotFoundError:
            sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    else:
        sys.stderr.write("Formato inválido\n")

        # https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
