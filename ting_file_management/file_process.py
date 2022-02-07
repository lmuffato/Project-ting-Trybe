import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.util import get_files_name


def process(path_file, instance):
    # RabbitMQ feels
    if path_file in get_files_name(instance):
        return None
    readed_file = txt_importer(path_file)
    msg = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(readed_file),
        "linhas_do_arquivo": readed_file
    }
    instance.enqueue(msg)
    sys.stdout.write(str(msg))


def remove(instance):
    if instance.__len__() > 0:
        consumer = instance.dequeue()["nome_do_arquivo"]
        return sys.stdout.write(f'Arquivo {consumer} removido com sucesso\n')
    sys.stdout.write('Não há elementos\n')


def file_metadata(instance, position):
    try:
        msg_in_queue = instance.search(position)
        sys.stdout.write(str(msg_in_queue))
    except IndexError:
        sys.stderr.write("Posição inválida")
