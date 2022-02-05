import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if instance.__len__() < 1:
        text = txt_importer(path_file)
        file_info = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(text),
            "linhas_do_arquivo": text,
        }
        instance.enqueue(file_info)
        sys.stdout.write(f"{file_info}")


def remove(instance):
    if len(instance) < 1:
        sys.stdout.write("Não há elementos\n")
    else:
        name = instance.search(0)["nome_do_arquivo"]
        instance.dequeue()
        sys.stdout.write(f"Arquivo {name} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        file_info = instance.search(position)
        sys.stdout.write(f"{file_info}")
    except IndexError:
        sys.stderr.write("Posição inválida")
