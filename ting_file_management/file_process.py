from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if path_file not in instance.list:
        instance.enqueue(path_file)
        txt = txt_importer(path_file)
        sys.stdout.write(str({
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(txt),
            "linhas_do_arquivo": txt
        }))


def remove(instance):
    if not instance.__len__():
        return sys.stdout.write('Não há elementos\n')
    path_file = instance.dequeue()
    return sys.stdout.write(f'Arquivo {path_file} removido com sucesso\n')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
