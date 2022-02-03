import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(instance.__len__()):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return None
    txt_file = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_file),
        "linhas_do_arquivo": txt_file
    }
    sys.stdout.write(str(data))
    instance.enqueue(data)


def remove(instance):
    length = instance.__len__()
    if length > 0:
        deque = instance.dequeue()['nome_do_arquivo']
        sys.stdout.write(
            f'Arquivo {deque} removido com sucesso\n'
        )
    else:
        return sys.stdout.write('Não há elementos\n')


def file_metadata(instance, position):
    try:
        txt_file = instance.search(position)
        if txt_file:
            data = {
                "nome_do_arquivo": txt_file["nome_do_arquivo"],
                "qtd_linhas": len(txt_file),
                "linhas_do_arquivo": txt_file
            }
            return sys.stdout.write(str(data))
    except IndexError:
        return sys.stderr.write('Posição inválida\n')
