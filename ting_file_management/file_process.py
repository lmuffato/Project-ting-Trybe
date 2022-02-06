import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    dados = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    instance.enqueue(dados)
    sys.stdout.write(str(dados))

    # requisitos feitos em consulta ao PR #02 da Marilia


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    try:
        dados = instance.dequeue()
        path_file = dados["nome_do_arquivo"]
        print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)
    except NotImplementedError:
        raise Exception


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        sys.stdout.write(str(data))
    except IndexError:
        sys.stderr.write("Posição inválida")
