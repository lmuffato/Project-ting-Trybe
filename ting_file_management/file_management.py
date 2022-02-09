# https://pt.stackoverflow.com/questions/226182/quebra-de-linha-em-um-arquivo-txt
# o link acima serviu para ter conhecimento da função splitlines()
# https://www.delftstack.com/pt/howto/python/python-print-to-stderr/
import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    try:
        if path_file.endswith('.txt'):
            txt_file = open(path_file, "r").read().splitlines()
            return list(txt_file)
        else:
            print("Formato inválido", file=sys.stderr)
    except IOError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
