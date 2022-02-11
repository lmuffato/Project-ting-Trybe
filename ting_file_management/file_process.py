import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    response = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }
    if response not in instance.fila:
        instance.enqueue(response)
    sys.stdout.write(str(response))


def remove(instance):
    if len(instance):
        content = instance.dequeue()
        file = content["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {file} removido com sucesso\n")
    else:
        sys.stdout.write("Não há elementos\n")
        return ("Não há elementos")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
    except IndexError:
        return sys.stderr.write("Posição inválida\n")
    else:
        sys.stdout.write(str(file))
