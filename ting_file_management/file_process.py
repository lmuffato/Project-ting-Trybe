import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    name_file = path_file.strip("../")
    length = len(instance)
    importer = txt_importer(path_file)

    if length == 0:
        file = {
            "nome_do_arquivo": path_file.strip("../"),
            "qtd_linhas": len(importer),
            "linhas_do_arquivo": importer
        }

        instance.enqueue(file)
        # https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print
        sys.stdout.write(str(file) + '\n')
        # ---------------------------------------------------------------------------------------------

    if length:
        search = instance.search(length)
        name_file_queue = search["nome_do_arquivo"]

        if name_file != name_file_queue:
            file = {
                "nome_do_arquivo": path_file.strip("../"),
                "qtd_linhas": len(importer),
                "linhas_do_arquivo": importer
            }

            instance.enqueue(file)
            sys.stdout.write(str(file) + '\n')


def remove(instance):
    length = len(instance)

    if length == 0:
        sys.stdout.write(str("Não há elementos" + '\n'))
    if length:
        name_text_delete = instance.dequeue()["nome_do_arquivo"]
        message = f"Arquivo {name_text_delete} removido com sucesso"

        sys.stdout.write(str(message + '\n'))


def file_metadata(instance, position):
    try:
        search = instance.search(position)

        file = {
           "nome_do_arquivo": search["nome_do_arquivo"],
           "qtd_linhas": search["qtd_linhas"],
           "linhas_do_arquivo": search["linhas_do_arquivo"]
        }

        sys.stdout.write(str(file) + '\n')
    except IndexError:
        print("Posição inválida", file=sys.stderr)
