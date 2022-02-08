from .file_management import txt_importer
import sys


def process(path_file, instance):

    data = txt_importer(path_file)

    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }

    instance.enqueue(result)

    sys.stdout.write(f"{result}")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
