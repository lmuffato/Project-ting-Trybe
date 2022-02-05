import sys


def validations(path_file):
    extension = path_file.split(".")
    if extension[-1] != "txt":
        return sys.stderr.write("Formato inválido\n")

    return False


def txt_importer(path_file):
    if not validations(path_file):
        try:
            data = open(path_file, "r")
            print(data)
        except FileNotFoundError:
            sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
