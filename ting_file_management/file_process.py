from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


queue_obj = Queue()


def process(path_file, queue_obj):
    for linha in queue_obj.queue:
        if linha['nome_do_arquivo'] == path_file:
            return
    dictio = {}
    dictio['nome_do_arquivo'] = path_file
    dictio['qtd_linhas'] = len(txt_importer(path_file))
    dictio['linhas_do_arquivo'] = txt_importer(path_file)
    queue_obj.enqueue(dictio)
    print(dictio)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
