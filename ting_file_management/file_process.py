import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for index in range(len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return None
    txt_import = txt_importer(path_file)
    processed_txt = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(txt_import),
        'linhas_do_arquivo': txt_import
    }
    instance.enqueue(processed_txt)
    sys.stdout.write(str(processed_txt))


def remove(instance):
    """Aqui irá sua implementação"""
    if not instance:
        return sys.stdout.write("Não há elementos\n")
    processed_txt = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {processed_txt} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
