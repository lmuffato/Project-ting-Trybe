import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    # """Aqui irá sua implementação"""
    # print(instance.search(0))
    # print(path_file)
    for index in range(len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return None

    text = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text),
        "linhas_do_arquivo": text,
    }
    instance.enqueue(data)
    return sys.stdout.write(f"{data}\n")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
