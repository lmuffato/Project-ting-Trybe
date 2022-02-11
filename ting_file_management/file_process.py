import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file)
    }
    if data not in instance._data:
        instance.enqueue(data)
    sys.stdout.write(str(data))


def remove(instance):
    if instance.is_empty():
        print("Não há elementos")
        return None

    value = instance.dequeue()
    name_file = value['nome_do_arquivo']
    print(f"Arquivo {name_file} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
