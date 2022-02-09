import re


def return_list_pathern(word, file_name, found):
    result = [
        {
            "palavra": word,
            "arquivo": file_name,
            "ocorrencias": found,
        }
    ]

    return result


def find_word(word, data):
    if re.search(word, data, re.IGNORECASE):
        return True


def exists_word(word, instance):
    data = instance.search(instance.__len__() - 1)
    index = 1
    aux = []

    for row in data["linhas_do_arquivo"]:
        result = find_word(word, row)
        if result:
            aux.append({"linha": index})
            index += 1
        else:
            index += 1

    return return_list_pathern(word, data["nome_do_arquivo"], aux)


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
