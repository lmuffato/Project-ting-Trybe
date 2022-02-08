# Requisito 2


# https://www.delftstack.com/pt/howto/python/python-print-to-stderr/#:~:text=stderr%20para%20imprimir%20para%20o,O%20m%C3%A9todo%20sys.
import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith(".txt"):
        # O método sys.stderr.write()imprime a mensagem como o parâmetro dado ao método stderr
        return sys.stderr.write("Formato inválido\n")
    try:
        # O splitlines()método divide uma string em uma lista. A divisão é feita em quebras de linha.
        with open(path_file, "r") as data:
            return data.read().splitlines()
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
