# from ting_file_management.queue import Queue
import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(file),
        'linhas_do_arquivo': file
    }
    instance.enqueue(data)
    print(data, file=sys.stdout)


def remove(instance):
    data = instance.dequeue()
    path_file = data['nome_do_arquivo']
    print(f'Arquivo {path_file} removido com sucesso\n', file=sys.stdout)


def file_metadata(instance, position):
    data = instance.search(position)
    print(data, file=sys.stdout)

# project = Queue()
# process('statics/arquivo_teste.txt', project)
# process('statics/arquivo_teste.txt', project)
