from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return None

    data = txt_importer(path_file)
    obj = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(data),
        'linhas_do_arquivo': data
    }
    instance.enqueue(obj)
    sys.stdout.write(str(obj))


def remove(instance):
    isEmpty = len(instance)

    if isEmpty == 0:
        return print('Não há elementos')

    obj = instance.dequeue()
    path_file = obj['nome_do_arquivo']

    print(f'Arquivo {path_file} removido com sucesso')


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        sys.stdout.write(str(data))
    except IndexError:
        sys.stderr.write('Posição inválida')
