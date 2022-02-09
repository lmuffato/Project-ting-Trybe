import sys


def txt_importer(path_file):
    stderr = sys.stderr
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=stderr)
    try:
        with open(path_file, mode="r") as tfile:
            content = tfile.read()
            return content.split("\n")
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=stderr)
