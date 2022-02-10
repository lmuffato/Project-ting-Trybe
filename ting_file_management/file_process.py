import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    content = txt_importer(path_file)
    file_lines = len(content)
    stdout = sys.stdout

    output_return = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": file_lines,
        "linhas_do_arquivo": content
    }

    if len(instance) > 0 and instance.search(0) == output_return:
        return print(output_return, file = stdout)

    instance.enqueue(output_return)
    print(output_return, file = stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
