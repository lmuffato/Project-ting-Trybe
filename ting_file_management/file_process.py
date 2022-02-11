import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for file in range(len(instance)):
        if instance.search(file)["nome_do_arquivo"] == path_file:
            return None

    doc = txt_importer(path_file)

    doc_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(doc),
        "linhas_do_arquivo": doc,
    }

    instance.enqueue(doc_data)

    return sys.stdout.write(str(doc_data))


def remove(instance):
    """Aqui irá sua implementação"""
    try:
        file = instance.dequeue()
        file_name = file["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {file_name} removido com sucesso\n")

    except Exception:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        file = instance.search(position)
        sys.stdout.write(str(file))
    except IndexError:
        sys.stderr.write("Posição inválida\n")
