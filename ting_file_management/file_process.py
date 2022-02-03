from .file_management import txt_importer
import sys


def process(path_file, instance):
    for position in range(len(instance)):
        if instance.search(position)['nome_do_arquivo'] == path_file:
            return None
    file_content = txt_importer(path_file)
    file_data = {
      "nome_do_arquivo": path_file,
      "qtd_linhas": len(file_content),
      "linhas_do_arquivo": file_content
    }
    instance.enqueue(file_data)
    print(file_data, file=sys.stdout)


def remove(instance):
    try:
        removed_object = instance.dequeue()
        path_file = removed_object['nome_do_arquivo']
    except IndexError:
        print('Não há elementos')
    else:
        print(f'Arquivo {path_file} removido com sucesso')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
