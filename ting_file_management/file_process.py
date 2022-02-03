import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file not in instance.list_ting:
        list_file = txt_importer(path_file)
        instance.enqueue(path_file)
        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(list_file),
            "linhas_do_arquivo": list_file
        }
        return sys.stdout.write(f"{data}")


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    else:
        path_file = instance.dequeue()
        return sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
