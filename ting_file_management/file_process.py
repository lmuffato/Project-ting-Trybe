import sys
from .file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    data = txt_importer(path_file)
    already_exists = False
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            already_exists = True
    if not already_exists:
        obj = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(data),
            "linhas_do_arquivo": data,
        }
        instance.enqueue(obj)
        sys.stdout.write(str(obj))


def remove(instance):
    """Aqui irá sua implementação"""
    try:
        path = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {path} removido com sucesso\n")
    except IndexError:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        position = instance.search(position)
        sys.stdout.write(f"{position}")
    except IndexError:
        sys.stderr.write("Posição inválida")
