from ting_file_management.file_management import txt_importer
from queue import Queue
import sys

def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None

    array_file = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(array_file),
        "linhas_do_arquivo": array_file,
    }

    instance.enqueue(data)

    sys.stdout.write(str(data))


def remove(instance):
    item_removed = instance.dequeue()

    if not item_removed:
        return sys.stdout.write("Não há elementos\n")

    file_name = item_removed["nome_do_arquivo"]
    
    sys.stdout.write(f"Arquivo {file_name} removido com sucesso\n")



def file_metadata(instance, position):
    try:
        info = instance.search(position)
        sys.stdout.write(str(info))
    except:
        sys.stderr.write("Posição inválida\n")

