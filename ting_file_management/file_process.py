
from ting_file_management import file_management
import sys


def process(path_file, instance):
    pathes = [
        instance.search(index)['nome_do_arquivo']
        for index in range(instance.__len__())
    ]

    if path_file in pathes:
        return None

    txt = file_management.txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt),
        "linhas_do_arquivo": txt
    }

    sys.stdout.write(str(data))
    instance.enqueue(data)


def remove(instance):
    """Aqui irá sua implementação"""
    if (instance.__len__() == 0):
        return print('Não há elementos')

    removed = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(
        f'Arquivo {removed} removido com sucesso\n'
    )


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        sys.stdout.write(str(data))
    except IndexError:
        sys.stderr.write('Posição inválida')
