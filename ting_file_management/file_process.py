from .file_management import txt_importer
import sys


def list_pathern(path, data):
    result = {
        "nome_do_arquivo": path,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }

    return result


def process(path_file, instance):

    data = txt_importer(path_file)

    result = list_pathern(path_file, data)

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
    if position > instance.__len__():
        return sys.stderr.write("Posição inválida")
    else:
        return sys.stdout.write(f"{instance.search(position)}")
