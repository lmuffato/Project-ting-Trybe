import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    file = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    instance.enqueue(data)
    sys.stdout.write(str(data))


def remove(instance):
    """Aqui irá sua implementação"""
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    try:
        data = instance.dequeue()
        path_file = data["nome_do_arquivo"]
        print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)
    except NotImplementedError:
        raise Exception


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        data = instance.search(position)
        sys.stdout.write(str(data))
    except IndexError:
        sys.stderr.write("Posição inválida")
