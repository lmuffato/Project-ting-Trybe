import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    file = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    enqueued = False
    for element in instance._data:
        if element["nome_do_arquivo"] == path_file:
            enqueued = True
            break
    if not enqueued:
        instance.enqueue(result)
    return print(result)


def remove(instance):
    """Aqui irá sua implementação"""
    if instance.__len__() == 0:
        return print("Não há elementos")
    file = instance._data[0]["nome_do_arquivo"]
    instance.dequeue()
    return print(f"Arquivo {file} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
