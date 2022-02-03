from ting_file_management import file_management


def exists_data(instance):
    for index in range(len(instance)-1):
        return instance.search(index)


def process(path_file, instance):
    file_lines = file_management.txt_importer(path_file)
    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines
    }
    if (instance.is_empty() or exists_data(instance)):
        instance.enqueue(file_data)
        print(file_data)


def remove(instance):
    pass


def file_metadata(instance, position):
    pass
