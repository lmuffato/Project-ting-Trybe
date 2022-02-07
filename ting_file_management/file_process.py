import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for row in instance.queue:
        if row['nome_do_arquivo'] == path_file:
            return
    the_dict = dict()
    the_dict['nome_do_arquivo'] = path_file
    the_dict['qtd_linhas'] = len(txt_importer(path_file))
    the_dict['linhas_do_arquivo'] = txt_importer(path_file)
    instance.enqueue(the_dict)
    print(the_dict)


def remove(instance):
    """Aqui irá sua implementação"""
    if instance.__len__() == 0:
        return print('Não há elementos')
    file = instance.dequeue()
    print(f'''Arquivo {file['nome_do_arquivo']} removido com sucesso''')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        item = instance.search(position)
        print(item)
    except IndexError:
        return sys.stderr.write('Posição inválida')
