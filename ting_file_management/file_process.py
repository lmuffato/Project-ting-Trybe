from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    size = len(instance)
    lines = txt_importer(path_file)
    infos = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(lines),
        'linhas_do_arquivo': lines,
    }

    for n in range(size):
        info = instance.search(n)
        if info['nome_do_arquivo'] == path_file:
            return

    instance.enqueue(infos)
    return print(infos, file=sys.stdout)


def remove(instance):
    try:
        file = instance.dequeue()
        path_file = file['nome_do_arquivo']
        print(f'Arquivo {path_file} removido com sucesso', file=sys.stdout)
    except IndexError:
        print('Não há elementos')


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        print(file, file=sys.stdout)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
