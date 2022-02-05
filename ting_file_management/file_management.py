import sys


# Print para strerr consultado em:
# https://www.delftstack.com/pt/howto/python/python-print-to-stderr/
def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, mode="r") as my_file:
            content = my_file.read()
            return content.split("\n")
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
