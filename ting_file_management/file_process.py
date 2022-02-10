import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)['nome_do_arquivo'] == path_file:
            return None
    import_file = txt_importer(path_file)
    processed_file = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(import_file),
        'linhas_do_arquivo': import_file
    }
    instance.enqueue(processed_file)
    sys.stdout.write(str(processed_file))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
