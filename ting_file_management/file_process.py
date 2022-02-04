import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if instance.__len__() < 1:
        text = txt_importer(path_file)
        file_info = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(text),
            "linhas_do_arquivo": text,
        }
        instance.enqueue(file_info)
        sys.stdout.write(f"{file_info}")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
