import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if not len(instance):  # if length == 0
        lines = txt_importer(path_file)
        processed_content = {
            "nome_do_arquivo": f"{path_file}",
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines,
        }
        instance.enqueue(processed_content)
        # source:
        # https://www.geeksforgeeks.org/how-to-print-to-stderr-and-stdout-in-python/
        print(
            processed_content,
            file=sys.stdout,
        )

    else:
        return instance


def remove(instance):
    if not len(instance):
        print("Não há elementos", file=sys.stdout)
    else:
        path_file = instance.search(0)["nome_do_arquivo"]
        print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)
        instance.dequeue


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
