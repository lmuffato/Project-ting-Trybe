from ting_file_management.queue import Queue


def exists_word(word, instance):
    result = {"palavra": word, "arquivo": "nome_do_arquivo", "ocorrencias": []}
    if len(result["ocorrencias"]) > 0:
        return result
    return list()


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


Queue = Queue()

print(exists_word("Acima", Queue))
