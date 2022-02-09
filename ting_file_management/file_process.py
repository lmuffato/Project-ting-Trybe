import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(len(instance)):
        if path_file == instance.search(i)['nome_do_arquivo']:
            return None

    read = txt_importer(path_file)
    mensagem = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(read),
        'linhas_do_arquivo': read
    }
    instance.enqueue(mensagem)
    print(mensagem)


def remove(instance):
    try:
        fileEx = instance.dequeue()
        print(
            'Arquivo {} removido com sucesso'
            .format(fileEx['nome_do_arquivo']))
    except Exception:
        print('Não há elementos')


def file_metadata(instance, position):
    try:
        return print(instance.search(position))
    except IndexError:
        print('Posição inválida', file=sys.stderr)
