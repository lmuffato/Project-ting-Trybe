import sys


def txt_importer(path_file):
    file_name, file_format = path_file.split(".")

    try:
        if (file_format != "txt"):
            print("Formato inválido", file=sys.stderr)

        with open(path_file) as file:
            content = file.read()
            return content.splitlines()

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
