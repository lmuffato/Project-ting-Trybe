import imp
from file_management import txt_importer
from queue import Queue

def process(path_file, instance):
    file_name = path_file.split("/")[-1]

    for i, _ in enumerate(instance):
        if instance.search(i)["nome_do_arquivo"] == file_name:
            return None

    array_file = txt_importer(path_file)

    data = {
        "nome_do_arquivo": file_name,
        "qtd_linhas": len(array_file),
        "linhas_do_arquivo": array_file,
    }

    instance.enqueue(data)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
