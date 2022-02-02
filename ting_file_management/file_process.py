import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file not in instance._list:
        instance.enqueue(path_file)
        info = txt_importer(path_file)
        answer_dict = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(info),
            "linhas_do_arquivo": info,
        }
        sys.stdout.write(str(answer_dict))


def remove(instance):
    if instance.__len__() == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        file_name = instance.dequeue()
        sys.stdout.write(f"Arquivo {file_name} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
