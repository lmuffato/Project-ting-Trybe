from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    if instance.__len__() < 1:
        arq = txt_importer(path_file)
        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(arq),
            "linhas_do_arquivo": arq,
        }
        instance.enqueue(data)
        return sys.stdout.write(f"{data}")


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) > 0:
        remove = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {remove} removido com sucesso\n")
    else:
        return sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
