import sys


def txt_importer(path_file):
    try:
        formatedText = list()
        if '.txt' not in path_file:
            return sys.stderr.write("Formato inválido\n")
        with open(path_file) as f:
            text = f.readlines()
            for line in text:
                formatedText.append(line.rstrip())
        return formatedText
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
