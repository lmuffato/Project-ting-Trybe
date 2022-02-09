import sys
from ting_file_management.file_management import txt_importer


def verify_item_already_exists(path_file, instance):
    for index in range(len(instance)):
        item = instance.search(index)

        if item["nome_do_arquivo"] == path_file:
            return True
    return False


def process(path_file, instance):
    file_content = txt_importer(path_file)

    file_already_exists = verify_item_already_exists(path_file, instance)

    if not file_already_exists:
        process_file = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file_content),
            "linhas_do_arquivo": file_content,
        }

        instance.enqueue(process_file)
        sys.stdout.write(str(process_file))


def remove(instance):
    try:
        removed_file = instance.dequeue()
        path_to_file = removed_file["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {path_to_file} removido com sucesso\n")
    except IndexError:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
