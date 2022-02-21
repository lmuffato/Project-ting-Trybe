import sys


def txt_importer(path_file):
    # Se o arquivo tiver a extensão txt.
    if not path_file.endswith('txt'):
        # retorna o erro no terminal
        return sys.stderr.write('Formato inválido\n')
    try:
        # Abrir o arquivo no modo leitura
        with open(path_file, mode="r") as file:
            # abre o arquivo, retornando um array onde cada elemento
            # é uma linha separada no split('\n')
            file_data = file.read().split('\n')
            return file_data
    # Se acontecer o a exception FileNotFoundError
    except FileNotFoundError:
        # retorna no terminal a mensagem
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')


# teste automatizado
# python3 -m pytest tests/test_file_mangement.py

# teste manual
# print(txt_importer("statics/arquivo_teste.txt"))
