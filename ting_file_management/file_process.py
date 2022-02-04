# from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(file),
        'linhas_do_arquivo': file
    }
    print(data)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""

# project = Queue()
# process('statics/arquivo_teste.txt', project)
