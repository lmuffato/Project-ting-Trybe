from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_already_exists = next(
        (
            file
            for file in instance.queue
            if file["nome_do_arquivo"] == path_file
        ),
        False,
    )
    if file_already_exists:
        return file_already_exists

    file_data = txt_importer(path_file)
    file_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_data),
        "linhas_do_arquivo": file_data,
    }
    instance.enqueue(file_dict)
    print(file_dict)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
