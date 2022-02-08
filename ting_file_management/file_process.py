import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file in [key["nome_do_arquivo"] for key in instance.queue_value]:
        return None

    data = txt_importer(path_file)

    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }

    instance.enqueue(result)
    return sys.stdout.write(str(result))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""