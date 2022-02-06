from .queue import Queue
from .file_management import txt_importer


def process(path_file, instance):
    file_content = txt_importer(path_file)
    json = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content
    }
    for i in instance._data:
        if i['nome_do_arquivo'] == path_file:
            return json
    Queue.enqueue(instance, json)
    return print(json)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
