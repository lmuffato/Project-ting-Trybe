import sys


def txt_importer(path_file):
    """sobre o stderr
    https://pythonguides.com/python-stderr-stdin-and-stdout/
    https://www.geeksforgeeks.org/how-to-print-to-stderr-and-stdout-in-python/
    """

    file_extension = path_file[len(path_file) - 4:len(path_file)]

    if file_extension != ".txt":
        return sys.stderr.write("Formato inválido\n")

    try:
        file_to_read = open(path_file, "r").read()
        return file_to_read.split("\n")
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
