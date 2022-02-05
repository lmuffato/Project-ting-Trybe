import sys


def check_if_path_exists(path):
    try:
        open(path, "r")
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path} não encontrado\n")


def validations(path_file):
    extension = path_file.split(".")
    if extension[-1] != "txt":
        return sys.stderr.write("Formato inválido\n")

    check_if_path_exists(path_file)
    return False


def txt_importer(path_file):
    if not validations(path_file):
        print("entrou")
