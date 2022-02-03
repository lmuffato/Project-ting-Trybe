from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if path_file not in instance.list:
        instance.enqueue(path_file)
        txt = txt_importer(path_file)
        sys.stdout.write(str({
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(txt),
            "linhas_do_arquivo": txt
        }))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
