import sys
from ting_file_management.file_management import txt_importer

list = []


def process(path_file, instance):
    if instance.__len__() == 0:
        file = txt_importer(path_file)
        list.append(path_file)

        response = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file
        }

        sys.stdout.write(f'{response}\n')

        instance.enqueue(response)
    else:
        pass


def remove(instance):
    if instance.__len__() == 0:
        sys.stdout.write('Não há elementos\n')
    else:
        instance.dequeue()
        path_name = list[0]
        list.remove(path_name)
        sys.stdout.write(f'Arquivo {path_name} removido com sucesso\n')


def file_metadata(instance, position):
    if position < 0 or position > len(list):
        sys.stderr.write('Posição inválida\n')
    else:
        sys.stdout.write(instance.search(position))
