import sys
from .file_management import txt_importer


def process(path_file, instance):
    if any(file['nome_do_arquivo'] == path_file for file in instance.data):
        return None

    content = txt_importer(path_file)
    data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(content),
        'linhas_do_arquivo': content,
    }
    instance.enqueue(data)
    return print(data)


def remove(instance):
    if not len(instance.data):
        return print('Não há elementos')
    delete = instance.dequeue()
    print(f"Arquivo {delete['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        instance.search(position)
    except IndexError:
        return sys.stderr.write('Posição inválida\n')
