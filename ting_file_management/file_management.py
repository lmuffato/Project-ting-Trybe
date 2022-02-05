import sys


def txt_importer(path_file):
    text = []
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file) as file:
            for line in file:
                text.append(line.replace("\n", ""))
            return text
    except FileNotFoundError:
        #https://www.delftstack.com/pt/howto/python/python-print-to-stderr/
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
