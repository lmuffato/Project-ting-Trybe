# Requisito 3

import sys
from .file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    # A range()função retorna uma sequência de números,
    #  começando em 0 por padrão e incrementa em 1 (por padrão)
    # e para antes de um número especificado.
    # E necessário fazer um for para percorrer os números

    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    result = {
        # Nome do arquivo recém adicionado
        "nome_do_arquivo": path_file,
        # Quantidade de linhas existentes no arquivo
        "qtd_linhas": len(txt_importer(path_file)),
        # linhas retornadas pela função do requisito 2
        "linhas_do_arquivo": txt_importer(path_file),
    }

    instance.enqueue(result)
    # stdouté usado para a saída de print()e instruções de expressão e para os
    # prompts de input()

    return sys.stdout.write(f"{result}\n")


# Requisito 4
def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    else:
        result = instance.dequeue()["nome_do_arquivo"]
        return sys.stdout.write(f"Arquivo {result} removido com sucesso\n")


# Requisito 5
def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        return sys.stdout.write(str(instance.search(position)))
    except IndexError:
        sys.stderr.write("Posição inválida\n")
