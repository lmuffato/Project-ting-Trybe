import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    content = txt_importer(path_file)
    new_dict = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(content),
        'linhas_do_arquivo': content
    }
    instance.enqueue(new_dict)
    print(new_dict, file=sys.stdout)


def remove(instance):
    try:
        removed = instance.dequeue()
        print(
            f"Arquivo {removed['nome_do_arquivo']} removido com sucesso",
            file=sys.stdout
        )
    except IndexError:
        print('Não há elementos', file=sys.stdout)


def file_metadata(instance, position):
    try:
        metadata = instance.search(position)
        print(metadata, file=sys.stdout)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
