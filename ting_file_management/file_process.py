import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for indice in range(len(instance)):
        if instance.search(indice)["nome_do_arquivo"] == path_file:
            return None
    file_txt = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_txt),
        "linhas_do_arquivo": file_txt,
    }
    instance.enqueue(result)
    sys.stdout.write(str(result))


def remove(instance):
    element = instance.dequeue()
    if element:
        print(f"Arquivo {element['nome_do_arquivo']} removido com sucesso")
    print("Não há elementos")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
