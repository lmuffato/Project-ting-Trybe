import sys
from ting_file_management.file_management import txt_importer


# Esta refatoração foi feita em Pair Programming
#  com Murilo Gonçalves ! Obrigado Murilo! :D <3
def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    txt_file = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_file),
        "linhas_do_arquivo": txt_file,
    }
    sys.stdout.write(str(data))
    instance.enqueue(data)


def remove(instance):
    if len(instance) > 0:
        removed = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {removed} removido com sucesso\n")
    else:
        return sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    try:
        answer = instance.search(position)
        if answer:
            data = {
                "nome_do_arquivo": answer["nome_do_arquivo"],
                "qtd_linhas": len(answer),
                "linhas_do_arquivo": answer,
            }
            return sys.stdout.write(str(data))
    except IndexError:
        sys.stderr.write("Posição inválida\n")
