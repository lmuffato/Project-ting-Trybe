from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for item in range(len(instance)):
        if instance.search(item)["nome_do_arquivo"] == path_file:
            return None

    txt_file = txt_importer(path_file)

    file_processed = {
      "nome_do_arquivo": path_file,
      "qtd_linhas": len(txt_file),
      "linhas_do_arquivo": txt_file,
    }

    instance.enqueue(file_processed)

    return sys.stdout.write(str(file_processed))


def remove(instance):
    try:
        file = instance.dequeue()
        file_name = file["nome_do_arquivo"]

    except Exception:
        sys.stdout.write("Não há elementos\n")

    else:
        sys.stdout.write(
            f"Arquivo {file_name} removido com sucesso\n"
          )


def file_metadata(instance, position):
    try:
        file = instance.search(position)
    except IndexError:
        sys.stderr.write("Posição inválida\n")
    else:
        sys.stdout.write(str(file))
