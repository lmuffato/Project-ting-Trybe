from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    content = txt_importer(path_file)
    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": content,
    }

    if len(instance) <= 0 or instance.search(0) != file_data:
        instance.enqueue(file_data)
        print(file_data)


def remove(instance):
    if len(instance) == 0:
        return print('Não há elementos')

    deleted_file = instance.dequeue()
    file_name = deleted_file['nome_do_arquivo']

    print(f'Arquivo {file_name} removido com sucesso')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
