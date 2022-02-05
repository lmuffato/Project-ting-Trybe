import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_content = txt_importer(path_file)
    lines_qty = len(file_content)
    result = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': lines_qty,
        'linhas_do_arquivo': file_content
    }

    exists = False
    for index in range(instance.__len__()):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            exists = True

    if not exists:
        instance.enqueue(result)
        print(result, file=sys.stdout)


def remove(instance):
    result = instance.dequeue()
    if result:
        print(f"Arquivo {result['nome_do_arquivo']} removido com sucesso")
    print('Não há elementos')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
