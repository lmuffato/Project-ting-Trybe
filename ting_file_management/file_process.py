import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    data = txt_importer(path_file)
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None
    obj = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data
    }
    instance.enqueue(obj)
    sys.stdout.write(str(obj))


def remove(instance):
    """Aqui irá sua implementação"""
    try:
        obj = instance.dequeue()
        path_file = obj["nome_do_arquivo"]
        sys.stdout.write(f'Arquivo {path_file} removido com sucesso')
    except IndexError:
        sys.stderr.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
