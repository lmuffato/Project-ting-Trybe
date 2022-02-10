from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    for index in range(len(instance)):
        # ignora arquivos com mesmo nome
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": (file),
        }

    instance.enqueue(data)
    return print(data)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
