import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""


def remove(instance):
    if len(instance) < 1:
        return "Não há elementos"
    result = instance.dequeue()
    print(f"Arquivo {result['nome_do_arquivo']} removido com sucesso")


# função inspirada na forma feita pelo João Andrade Jr
def file_metadata(instance, position):
    if position > instance.__len__():
        return sys.stderr.write("Posição inválida")
    else:
        data = instance.search(position)
        print(data, sys.stdout)
