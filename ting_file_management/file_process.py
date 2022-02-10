import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_content = txt_importer(path_file)

    output = {"nome_do_arquivo": path_file,
              "qtd_linhas": len(file_content),
              "linhas_do_arquivo": file_content
              }

    if len(instance) > 0 and instance.search(0) == output:
        print(output)
    else:
        instance.enqueue(output)
        print(output)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        removed_file = instance.dequeue()
        file_name = removed_file["nome_do_arquivo"]
        print(f"Arquivo {file_name} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        print(data)
    except IndexError:
        sys.stderr.write("Posição inválida")
