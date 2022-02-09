import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    data = txt_importer(path_file)
    dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }
    for index in instance.queue:
        if dict["nome_do_arquivo"] == index["nome_do_arquivo"]:
            return None
    else:
        instance.enqueue(dict)
        sys.stdout.write(str(dict))


def remove(instance):
    if instance.__len__() == 0:
        return print("Não há elementos")
    rm_file = instance.dequeue()
    print(rm_file)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
