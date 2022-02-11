from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    lines = txt_importer(path_file)
    single_file = True
    file_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }
    for file in instance.data:
        if file["nome_do_arquivo"] == path_file:
            single_file = False
    if single_file:
        instance.enqueue(file_dict)
        print(file_dict)


def remove(instance):
    if len(instance.data) == 0:
        print("Não há elementos")
        return
    file = instance.dequeue()
    path_file = file["nome_do_arquivo"]
    print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        print(file)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
