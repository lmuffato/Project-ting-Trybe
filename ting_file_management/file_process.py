import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    lines = txt_importer(path_file)
    if lines:
        content = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines,
        }
        for file in instance.queue:
            if file["nome_do_arquivo"] == path_file:
                return None

        instance.enqueue(content)
        sys.stdout.write(str(content))


def remove(instance):
    """Aqui irá sua implementação"""
    try:
        instance.dequeue()
        sys.stdout.write(
            "Arquivo statics/arquivo_teste.txt removido com sucesso\n"
        )
    except IndexError:
        sys.stdout.write(
            "Não há elementos\n"
        )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
