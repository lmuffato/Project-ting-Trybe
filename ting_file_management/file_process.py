from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    text_lines = txt_importer(path_file)

    file_summary = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(text_lines),
        'linhas_do_arquivo': text_lines
    }

    for entry in instance._data:
        if entry == file_summary:
            return None

    instance.enqueue(file_summary)

    print(file_summary)


def remove(instance):
    if instance.__len__() == 0:
        print('Não há elementos')
        return None

    removed = instance.dequeue()
    removed_file_name = removed['nome_do_arquivo']

    print(f'Arquivo {removed_file_name} removido com sucesso')


def file_metadata(instance, position):
    try:
        value = instance.search(position)
        print(value)
    except IndexError:
        sys.stderr.write('Posição inválida')
