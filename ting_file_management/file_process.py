from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }

    if result not in instance.data:
        instance.enqueue(result)

    return sys.stdout.write(str(result))


def remove(instance):
    element = instance.dequeue()

    if element is None:
        return sys.stdout.write("Não há elementos\n")

    return sys.stdout.write(
        f"Arquivo {element['nome_do_arquivo']} removido com sucesso\n"
    )


def file_metadata(instance, position):
    try:
        element = instance.search(position)
    except IndexError:
        return sys.stderr.write("Posição inválida\n")
    else:
        return sys.stdout.write(str(element))
