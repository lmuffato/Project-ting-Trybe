import sys


def txt_importer(path_file):
    if path_file.endswith('.txt'):
        try:
            txt_file = open(path_file, "r")
            return txt_file.read().splitlines()
        except FileNotFoundError:
            # print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
            sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
    else:
        # print("Formato inválido", file=sys.stderr)
        sys.stderr.write('Formato inválido\n')

# Source:
# https://docs.python.org/3.0/library/sys.html#module-sys
# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
