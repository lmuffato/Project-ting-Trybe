from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for file in instance.fila:
        if path_file == file["nome_do_arquivo"]:
            return None

    resultado = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }

    instance.enqueue(resultado)
    sys.stdout.write(str(resultado))


def remove(instance):
    if not instance.__len__():
        return sys.stdout.write("Não há elementos\n")
    resultado = instance.dequeue()["nome_do_arquivo"]
    return sys.stdout.write(f"Arquivo {resultado} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        resultado = instance.search(position)
        sys.stdout.write(str(resultado))
    except IndexError:
        sys.stderr.write("Posição inválida\n")
