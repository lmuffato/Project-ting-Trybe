from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for linha in instance.queue:
        if linha['nome_do_arquivo'] == path_file:
            return
    dictio = {}
    dictio['nome_do_arquivo'] = path_file
    dictio['qtd_linhas'] = len(txt_importer(path_file))
    dictio['linhas_do_arquivo'] = txt_importer(path_file)
    instance.enqueue(dictio)
    print(dictio)


def remove(instance):
    if instance.__len__() == 0:
        return print('Não há elementos')
    file = instance.dequeue()
    print(f'''Arquivo {file['nome_do_arquivo']} removido com sucesso''')


def file_metadata(instance, position):
    try:
        item = instance.search(position)
        print(item)
    except IndexError:
        return sys.stderr.write('Posição inválida')
