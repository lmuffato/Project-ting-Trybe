def exists_word(word, instance):
    """começando"""
    result = list()
    for element in instance._data:
        object = {
            "palavra": word,
            "arquivo": element["nome_do_arquivo"],
            "ocorrencias": list(),
        }
    for index, line in enumerate(element["linhas_do_arquivo"]):
        if word in line:
            res = {"linha": index + 1}
            object["ocorrencias"].append(res)
        else:
            return []
        result.append(object)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
