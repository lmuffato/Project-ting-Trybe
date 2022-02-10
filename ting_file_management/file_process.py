from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)
    for index in range(len(instance)):
        # ignora arquivos com mesmo nome
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": (file),
        }

    instance.enqueue(data)
    return print(data)


def remove(instance):
    if not instance:
        return sys.stdout.write("Não há elementos\n")
    remove = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {remove} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        # print(instance.search(position))
        sys.stdout.write(str(instance.search(position)))
        # transforma em string pq o print nao pode
    except IndexError:
        return sys.stderr.write("Posição inválida\n")
