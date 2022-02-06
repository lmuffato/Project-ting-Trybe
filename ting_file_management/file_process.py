import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance):
    data = txt_importer(path_file)
    result = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(data),
        'linhas_do_arquivo': data,
    }
    for index in instance.queue:
        if result['nome_do_arquivo'] == index['nome_do_arquivo']:
            return None
    else:
        instance.enqueue(result)
        sys.stdout.write(str(result))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


Queue = Queue()
print(process("statics/arquivo_teste.txt", Queue))
