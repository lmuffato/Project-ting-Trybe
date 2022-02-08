import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    data = list()
    try:
        if path_file.endswith(".txt"):
            with open(path_file, "r") as file:
                for line in file.readlines():
                    formated_line = line.strip("\n")
                    data.append(formated_line)
                return data
        else:
            sys.stderr.write("Formato inválido\n")
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
