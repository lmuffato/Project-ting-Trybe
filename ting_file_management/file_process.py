import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    instance.enqueue(path_file)
    return print(
        f"'nome_do_arquivo': '{path_file}'\n",
        f"'qtd_linhas': {len(txt_importer(path_file))}\n",
        f"'linhas_do_arquivo': {txt_importer(path_file)}\n",
        file=sys.stdout,
    )


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
