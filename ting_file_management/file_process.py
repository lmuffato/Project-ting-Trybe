from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    text_content = txt_importer(path_file)

    output = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text_content),
        "linhas_do_arquivo": text_content
    }

    if len(instance) > 0 and instance.search(0) == text_content:
        return print(output)

    instance.enqueue(text_content)
    print(output)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
