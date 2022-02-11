import sys


def txt_importer(path_file):
    try:
        if ".txt" not in path_file:
            print("Formato inválido", file=sys.stderr)
            return
        with open(path_file) as file:
            lines = [line.rstrip() for line in file]
        file.close()
        return lines
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
