import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")

    try:
        with open(path_file, "r") as fileDataTxt:
            return fileDataTxt.read().splitlines()

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
