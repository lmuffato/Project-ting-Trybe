import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file: str, instance: Queue):
    for index in range(len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return None
    file_data = txt_importer(path_file)
    processed_data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(file_data),
        'linhas_do_arquivo': file_data
    }
    instance.enqueue(processed_data)
    print(processed_data, file=sys.stdout)


def remove(instance: Queue):
    file_data = instance.dequeue()
    if file_data is None:
        print('Não há elementos', file=sys.stdout)
        return None
    path_file = file_data['nome_do_arquivo']
    print(f'Arquivo {path_file} removido com sucesso', file=sys.stdout)


def file_metadata(instance: Queue, position: int):
    try:
        file_data = instance.search(position)
        print(file_data, file=sys.stdout)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
