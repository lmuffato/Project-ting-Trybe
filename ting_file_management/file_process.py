from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    linhas = txt_importer(path_file)
    qtd = len(linhas)
    output = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": qtd,
        "linhas_do_arquivo": linhas
    }

    try:
        existing = instance.search(0)
        if existing['nome_do_arquivo'] != path_file:
            instance.enqueue(output)
            print(output)
    except IndexError:
        instance.enqueue(output)
        print(output)


def remove(instance):
    try:
        existing = instance.dequeue()
        print("Arquivo " + existing['nome_do_arquivo'] +
              " removido com sucesso")
    except IndexError:
        print("Não há elementos")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
