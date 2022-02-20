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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
