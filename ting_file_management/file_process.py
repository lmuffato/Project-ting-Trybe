import sys
# from queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    name_file = path_file.strip("../")
    length = len(instance)
    importer = txt_importer(path_file)

    if length == 0:
        file = {
            "nome_do_arquivo": path_file.strip("../"),
            "qtd_linhas": len(importer),
            "linhas_do_arquivo": importer
        }

        instance.enqueue(file)
        sys.stdout.write(str(file) + '\n')

    if length:
        search = instance.search(length)
        name_file_queue = search["nome_do_arquivo"]

        if name_file != name_file_queue:
            file = {
                "nome_do_arquivo": path_file.strip("../"),
                "qtd_linhas": len(importer),
                "linhas_do_arquivo": importer
            }

            instance.enqueue(file)
            sys.stdout.write(str(file) + '\n')


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""

# fila = Queue()

# pathOne = "../test.txt"
# pathTwo = "../hello.txt"

# process(pathOne, fila)
# process(pathOne, fila)
# print(process(pathTwo, fila))
# print(len(fila))
