import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for data in instance.data:
        if data["nome_do_arquivo"] == path_file:
            return None
    data = txt_importer(path_file)
    content = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }
    instance.enqueue(content)
    sys.stdout.write(str(content))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
