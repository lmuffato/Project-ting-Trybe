from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for index in range(len(instance)):
        if path_file == instance.search(index)["nome_do_arquivo"]:
            return None

    file = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    instance.enqueue(data)
    print(data)


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        return print("Não há elementos")

    file = instance.dequeue()["nome_do_arquivo"]
    print(f'Arquivo {file} removido com sucesso')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        file = instance.search(position)
        print(file)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
