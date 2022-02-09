import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
    try:
        file = open(path_file, "r")
        file_content = file.read()
        lines = file_content.split("\n")
        file.close()
        return lines
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
