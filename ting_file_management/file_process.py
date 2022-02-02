import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    instance.enqueue(path_file)
    info = txt_importer(path_file)
    answer_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(info),
        "linhas_do_arquivo": info,
    }
    sys.stdout.write(str(answer_dict))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
