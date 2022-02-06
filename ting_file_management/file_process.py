import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return None

    output = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(txt_importer(path_file)),
        'linhas_do_arquivo': txt_importer(path_file)
    }

    sys.stdout.write(str(output))
    instance.enqueue(output)


def remove(instance):
    if not instance:
        return sys.stdout.write("Não há elementos\n")

    remove = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(
      f"Arquivo {remove} removido com sucesso\n"
      )


def file_metadata(instance, position):
    try:
        return sys.stdout.write(str(instance.search(position)))
    except IndexError:
        return sys.stderr.write('Posição inválida\n')
