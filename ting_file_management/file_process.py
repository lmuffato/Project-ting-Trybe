from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    text_content = txt_importer(path_file)

    output = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text_content),
        "linhas_do_arquivo": text_content
    }

    if len(instance) > 0 and instance.search(0) == output:
        return print(output)

    instance.enqueue(output)
    print(output)


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos")

    removed_file = instance.dequeue()
    file_name = removed_file["nome_do_arquivo"]
    print(f"Arquivo {file_name} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
