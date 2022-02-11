import sys
from ting_file_management import file_management


def process(path_file, instance):
    dataFileTxt = file_management.txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(dataFileTxt),
        "linhas_do_arquivo": dataFileTxt,
    }

    for item in range(0, instance.__len__()):
        if path_file == instance.search(item)["nome_do_arquivo"]:
            return None

    sys.stdout.write(str(data))
    instance.enqueue(data)


def remove(instance):
    if instance.__len__() <= 0:
        sys.stdout.write("Não há elementos\n")
        return

    elementRemoved = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {elementRemoved} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        sys.stdout.write(str(data))
    except IndexError:
        sys.stderr.write("Posição inválida\n")
