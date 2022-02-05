import sys


def validations(path_file):
    extension = path_file.split(".")
    if extension[-1] != "txt":
        return sys.stderr.write("Formato inválido\n")

    return False


# pesquisa sobre leitura de arquivo txt em:
# https://www.kite.com/python/answers/how-to-read-a-newline-delimited-text-file-in-python
def txt_importer(path_file):
    if not validations(path_file):
        try:
            data = open(path_file)
            final_list = data.read()

            return final_list.splitlines()

        except FileNotFoundError:
            sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
