import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    doc = txt_importer(path_file)

    doc_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(doc),
        "linhas_do_arquivo": doc,
    }

    instance.enqueue(doc_data)

    return sys.stdout.write(str(doc_data))



def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
