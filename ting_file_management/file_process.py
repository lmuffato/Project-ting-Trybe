import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if not len(instance):  # if length == 0
        lines = txt_importer(path_file)
        instance.enqueue(lines)
        # source:
        # https://www.geeksforgeeks.org/how-to-print-to-stderr-and-stdout-in-python/
        print(
            {
                "nome_do_arquivo": f"{path_file}",
                "qtd_linhas": len(lines),
                "linhas_do_arquivo": lines,
            },
            file=sys.stdout,
        )

    else:
        return instance


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
