from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    data = txt_importer(path_file)

    file_to_compare = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(data),
        'linhas_do_arquivo': data
    }

    for text in instance.data:
        if text == file_to_compare:
            return None

    instance.enqueue(file_to_compare)

    print(file_to_compare)


def remove(instance):
    if not instance.__len__():
        print('Não há elementos')
        return None

    file = instance.dequeue()

    print(f"Arquivo {file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        value = instance.search(position)
        print(value)
    except IndexError:
        sys.stderr.write('Posição inválida')
