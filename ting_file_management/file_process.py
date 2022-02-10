import sys
from ting_file_management.file_management import txt_importer

# função inspirada na forma feita pelo Jodiel


def process(path_file, instance):
    size = len(instance)
    for index in range(size):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return None
    result = txt_importer(path_file)
    data_to_write = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(result),
        'linhas_do_arquivo': result
    }
    instance.enqueue(data_to_write)
    sys.stdout.write(str(data_to_write))


def remove(instance):
    if len(instance) < 1:
        return sys.stdout.write('Não há elementos\n')
    result = instance.dequeue()
    print(f"Arquivo {result['nome_do_arquivo']} removido com sucesso")


# função inspirada na forma feita pelo João Andrade Jr
def file_metadata(instance, position):
    if position > instance.__len__():
        return sys.stderr.write("Posição inválida")
    else:
        data = instance.search(position)
        print(data, sys.stdout)
