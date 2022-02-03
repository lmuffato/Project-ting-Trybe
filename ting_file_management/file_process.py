import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file not in instance.list:
        instance.enqueue(path_file)
        data = txt_importer(path_file)
        data_format = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(data),
            "linhas_do_arquivo": data
        }
        return sys.stdout.write(str(data_format))


def remove(instance):
    try:
        delFile = instance.dequeue()
        return sys.stdout.write(f'Arquivo {delFile} removido com sucesso\n')
    except IndexError:
        return print('Não há elementos')


def file_metadata(instance, position):
    try:
        path_file = instance.search(position)
        data = txt_importer(path_file)
        data_format = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(data),
            "linhas_do_arquivo": data
        }
        return sys.stdout.write(str(data_format))
    except IndexError:
        sys.stderr.write("Posição inválida")
