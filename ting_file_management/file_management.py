import sys


def txt_importer(path_file):
    content_file = []

    if not path_file.endswith('.txt'):
        sys.stderr.write('Formato inválido\n')

    try:
        with open(path_file, mode="r") as file:
            text_content = [line.rstrip('\n') for line in file]

            content_file = text_content
            file.close()

    except FileNotFoundError:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')

    finally:
        return content_file

# Conseguir extrair as linhas sem os espaços com a explicação:
# https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
