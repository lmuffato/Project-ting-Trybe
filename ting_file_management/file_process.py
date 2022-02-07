from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    data = txt_importer(path_file)
    data_details = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }
    for el in instance.data:
        if path_file == el["nome_do_arquivo"]:
            return False

    instance.enqueue(data_details)
    return sys.stdout.write(f"{data_details}\n")


def remove(instance):
    if not len(instance):
        return sys.stdout.write("Não há elementos\n")
    file_removed = instance.dequeue()["nome_do_arquivo"]
    return sys.stdout.write(
        f"Arquivo {file_removed} removido com sucesso\n"
    )


def file_metadata(instance, position):
    try:
        info = instance.search(position)
        sys.stdout.write(f"{info}\n")
    except IndexError:
        sys.stderr.write("Posição inválida")
