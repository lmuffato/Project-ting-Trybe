from sys import stdout
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    lines = txt_importer(path_file)
    print_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }
    print(print_dict)
    mapped = list(map(lambda x: x["nome_do_arquivo"], instance.queue))
    if path_file in mapped:
        return None
    instance.enqueue(print_dict)
    for key in print_dict.keys():
        print(f'{key}:{print_dict[key]}', file=stdout)


def remove(instance):
    if len(instance.queue) < 1:
        print('Não há elementos')
        return None
    removed = instance.dequeue()
    name = removed["nome_do_arquivo"]
    print(f'Arquivo {name} removido com sucesso')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
