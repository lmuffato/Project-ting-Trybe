import imp
from file_management import txt_importer
from queue import Queue

def process(path_file, instance):
    array_file = txt_importer(path_file)
    for item in array_file:
        instance.enqueue(item)
    
    return {
        "nome_do_arquivo": path_file.split("/")[-1],
        "qtd_linhas": len(instance),
        "linhas_do_arquivo": array_file,
    }

""" queue = Queue()
x = process("dev-requirements.txt", queue)
print(x) """



def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
