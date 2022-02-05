import sys


def validations(path_file):
    extension = path_file.split(".")
    if extension[-1] != "txt":
        return sys.stderr.write("Formato inválido\n")

    return True


def txt_importer(path_file):
    validated = validations(path_file)
    if validated is str:
        return validated
