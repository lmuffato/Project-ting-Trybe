import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file not in instance.list:
        instance.enqueue(path_file)
        file_data = txt_importer(path_file)
        result_dict = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file_data),
            "linhas_do_arquivo": file_data,
        }
        sys.stdout.write(str(result_dict))


def remove(instance):
    try:
        remove_object = instance.dequeue()
        deleted_file = remove_object
    except IndexError:
        print('Não há elementos')
    else:
        print(f'Arquivo {deleted_file} removido com sucesso\n')


def file_metadata(instance, position):
    try:
        file_metadata = instance.search(position)
        info = txt_importer(file_metadata)
        result_dict = {
            "nome_do_arquivo": file_metadata,
            "qtd_linhas": len(info),
            "linhas_do_arquivo": info,
        }
        sys.stdout.write(str(result_dict))
    except IndexError:
        sys.stderr.write('Posição inválida\n')
