import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    instance.enqueue(path_file)
    return print(
        f"'nome_do_arquivo': '{path_file}'\n",
        f"'qtd_linhas': {len(txt_importer(path_file))}\n",
        f"'linhas_do_arquivo': {txt_importer(path_file)}\n",
        file=sys.stdout,
    )


def remove(instance):
    if len(instance) != 0:
        removed = instance.dequeue()
        sys.stdout.write(f"Arquivo {removed} removido com sucesso\n")
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    try:
        answer = instance.search(position)
        sys.stdout.write(answer)
    except IndexError:
        sys.stderr.write("Posição inválida")
