from ting_file_management.file_management import txt_importer
import sys


# retorno esperado
# {
# "nome_do_arquivo": "arquivo_teste.txt",
# "qtd_linhas": 3,
# "linhas_do_arquivo": [...]
# }


def process(path_file, instance):
    readedFile = txt_importer(path_file)
    # Fonte: https://blog.betrybe.com/python/python-range/
    for item in range(0, instance.__len__()):
        if path_file == instance.search(item)["nome_do_arquivo"]:
            return None

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(readedFile),
        "linhas_do_arquivo": readedFile,
    }

    # Fontes: https://docs.python.org/3/library/sys.html
    # https://www.geeksforgeeks.org/queue-in-python/
    sys.stdout.write(f"{data}\n")
    return instance.enqueue(data)


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")

    # Fonte: https://www.geeksforgeeks.org/queue-in-python/
    elementToRemove = instance.dequeue()["nome_do_arquivo"]
    return sys.stdout.write(
        f"Arquivo {elementToRemove} removido com sucesso\n"
    )


def file_metadata(instance, position):
    # Em caso da posição não existir, deve ser exibida uma mensagem de erro:
    # "Posição inválida" na stderr.
    try:
        return sys.stdout.write(f"{instance.search(position)}")
    except IndexError:
        return sys.stderr.write('Posição inválida\n')
