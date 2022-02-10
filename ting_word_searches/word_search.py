import re


def searching_and_counting_word(data, word, index):
    quantity = []
    list = []
    for line in data["linhas_do_arquivo"]:
        if re.search(word, line, re.IGNORECASE):
            quantity.append({"linha": index + 1})
            list.append(
                {
                    "palavra": f"{word}",
                    "arquivo": data["nome_do_arquivo"],
                    "ocorrencias": quantity,
                }
            )
    return list


def exists_word(word, instance):
    for index in range(len(instance)):
        data = instance.search(index)
        result = searching_and_counting_word(data, word, index)
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
