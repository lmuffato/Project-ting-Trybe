import sys

def txt_importer(path_file):
    if path_file.split('.')[1] != 'txt':
        return sys.stderr.write("Formato inválido")

    try:
        with open(path_file, "r") as file:
            my_file = file.read()
            return my_file.split('\n')
    except:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado")

