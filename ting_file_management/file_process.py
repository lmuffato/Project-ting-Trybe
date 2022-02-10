import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    response = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }
    if response not in instance.fila:
        instance.enqueue(response)
    sys.stdout.write(str(response))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
