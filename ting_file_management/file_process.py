from .file_management import txt_importer
import sys


def process(path_file, instance):

    data = txt_importer(path_file)

    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }

    instance.enqueue(result)

    sys.stdout.write(f"{result}")


def remove(instance):
    if instance.__len__() != 0:
        removed = instance.dequeue()
        file_name = removed["nome_do_arquivo"]

        return sys.stdout.write(f"Arquivo {file_name} removido com sucesso\n")
    else:
        return sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
