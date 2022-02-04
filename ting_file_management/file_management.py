import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith("txt"):
            sys.stderr.write("Formato inválido\n")
        with open(path_file, "r", encoding="UTF-8") as file:
            text = file.read().splitlines()
            return text
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
