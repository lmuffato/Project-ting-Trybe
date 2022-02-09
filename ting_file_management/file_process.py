import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file not in instance.queue:
        txt_file = txt_importer(path_file)
        instance.enqueue(path_file)
        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(txt_file),
            "linhas_do_arquivo": txt_file
        }
        return sys.stdout.write(f"{data}")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
