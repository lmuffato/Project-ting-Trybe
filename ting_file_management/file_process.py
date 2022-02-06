import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance):
    data = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }
    for index in instance.queue:
        if result["nome_do_arquivo"] == index["nome_do_arquivo"]:
            return None
    else:
        instance.enqueue(result)
        sys.stdout.write(str(result))


def remove(instance):
    if instance.__len__() > 0:
        remove_item = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {remove_item} removido com sucesso\n")
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    try:
        item = instance.search(position)
        sys.stdout.write(str(item))
    except IndexError:
        sys.stderr.write("Posição inválida\n")


Queue = Queue()
print(process("statics/arquivo_teste.txt", Queue))
