import sys
from ting_file_management.file_management import txt_importer

def process(path_file, instance):
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
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    try:
        removed_pop = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {removed_pop} removido com sucesso\n")
    except NotImplementedError:
        raise 


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        sys.stdout.write(str(data))
    except IndexError:
        # https://www.youtube.com/watch?v=GiGVT6BjjO0
        sys.stderr.write("Posição inválida")