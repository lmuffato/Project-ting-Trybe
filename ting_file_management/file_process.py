from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    info_file = txt_importer(path_file)

    info_return = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(info_file),
        "linhas_do_arquivo": info_file
    }

    for index in instance._data:
        if index["nome_do_arquivo"] == path_file:
            return None

    instance.enqueue(info_return)
    print(info_return, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""
    if not instance._data:
        print("Não há elementos", file=sys.stdout)



def file_metadata(instance, position):
    """Aqui irá sua implementação"""
