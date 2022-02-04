from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if path_file not in instance.head_value:
        instance.enqueue(path_file)
        data = txt_importer(path_file)
        output = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(data),
            "linhas_do_arquivo": data,
        }
        return sys.stdout.write(str(output))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
