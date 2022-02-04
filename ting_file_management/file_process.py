from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):

    txt_file = txt_importer(path_file)

    file_processed = {
      "nome_do_arquivo": path_file,
      "qtd_linhas": len(txt_file),
      "linhas_do_arquivo": txt_file,
    }

    instance.enqueue(file_processed)

    return sys.stdout.write(str(file_processed))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
