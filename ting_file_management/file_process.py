import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for data in range(instance.__len__()):
        if instance.search(data)['nome_do_arquivo'] == path_file:
            return None
    file = txt_importer(path_file)
    data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(file),
        'linhas_do_arquivo': file
    }
    instance.enqueue(data)
    print(data, file=sys.stdout)


def remove(instance):
    try:
        data = instance.dequeue()
        path_file = data['nome_do_arquivo']
        print(f'Arquivo {path_file} removido com sucesso\n', file=sys.stdout)
    except Exception:
        print('Não há elementos', file=sys.stdout)


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        print(data, file=sys.stdout)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
