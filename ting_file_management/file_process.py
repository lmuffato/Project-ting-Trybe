import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    # https://www.w3schools.com/python/ref_func_range.asp
    # class range(stop: int) - Thx VSCode
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
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    itemToRemove = instance.dequeue()
    file_path = itemToRemove["nome_do_arquivo"]
    print(f"Arquivo {file_path} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        sys.stdout.write(str(data))
    except IndexError:
        sys.stderr.write("Posição inválida")
