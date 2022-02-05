import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_content = txt_importer(path_file)
    lines_qty = len(file_content)
    result = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': lines_qty,
        'linhas_do_arquivo': file_content
    }
    instance.enqueue(result)
    print(result, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
