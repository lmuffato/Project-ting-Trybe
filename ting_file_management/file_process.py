import sys
from .file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if path_file in instance.search(index)["nome_do_arquivo"]:
            return None

    file = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    instance.enqueue(data)
    print(data, file=sys.stdout)


def remove(instance):
    if len(instance) <= 0:
        print("Não há elementos", file=sys.stdout)
    else:
        item_removed = instance.dequeue()
        print(
            f"Arquivo {item_removed['nome_do_arquivo']} removido com sucesso",
            file=sys.stdout,
        )


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        print(data, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
