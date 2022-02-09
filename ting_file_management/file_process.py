import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)['nome_do_arquivo'] == path_file:
            return None

    imp_txt = txt_importer(path_file)
    res = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(imp_txt),
        'linhas_do_arquivo': imp_txt
    }
    instance.enqueue(res)
    sys.stdout.write(str(res))


def remove(instance):
    if not instance:
        return sys.stdout.write("Não há elementos\n")
    remove_queue = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {remove_queue} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
