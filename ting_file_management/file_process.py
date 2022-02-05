import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
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
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    element = instance.dequeue()
    element_title = element["nome_do_arquivo"]
    sys.stderr.write(f"Arquivo {element_title} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
