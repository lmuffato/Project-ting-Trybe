from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    text_importer = txt_importer(path_file)
    response = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text_importer),
        "linhas_do_arquivo": text_importer
    }

    list_name_files = [file["nome_do_arquivo"] for file in instance.queue]

    if path_file not in list_name_files:
        instance.enqueue(response)

    return sys.stdout.write(str(response))


def remove(instance):
    """Aqui irá sua implementação"""
    if not instance.__len__():
        return sys.stdout.write("Não há elementos\n")

    file = instance.dequeue()
    file_name = file["nome_do_arquivo"]
    return sys.stdout.write(f"Arquivo {file_name} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        found = instance.search(position)
        return sys.stdout.write(str(found))
    except IndexError:
        return sys.stderr.write("Posição inválida")
