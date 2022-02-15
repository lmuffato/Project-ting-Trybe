import pathlib
import sys


def inport_news(path_file):
    try:
        with open(path_file, "r") as file:
            data = file.read()
            file_lines = data.split("\n")
            return file_lines

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")


def txt_importer(path_file):
    if path_file:
        if_correct_path = {
            ".txt": inport_news(path_file),
        }

        try:
            extension = pathlib.Path(path_file).suffix
            call_function = if_correct_path[extension]
            return call_function

        except KeyError:
            sys.stderr.write("Formato inválido\n")

    else:
        print("Arquivo não encontrado")
