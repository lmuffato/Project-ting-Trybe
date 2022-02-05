import sys

# Impressao de stderr encontrado no link:
# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python


def txt_importer(path_file):
    if ".txt" not in path_file:
        return sys.stderr.write("Formato inválido\n")
    try:
        data = []
        with open(path_file, "r") as file:
            for row in file:
                data.append(row.replace("\n", ""))
        return data
    except FileNotFoundError:
        return sys.stderr.write("Arquivo " + path_file + " não encontrado\n")
