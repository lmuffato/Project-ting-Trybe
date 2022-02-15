def exists_word(word, instance):
    word_occurrencies = list()
    length = instance.__len__()
    if not length:
        return word_occurrencies
    else:
        occurrencies = list()
        content = instance.search(0)
        for index, words in enumerate(content["linhas_do_arquivo"]):
            if word.lower() in words.lower():
                occurrencies.append({"linha": index + 1})
        if occurrencies:
            word_occurrencies.append(
                {
                    "palavra": word,
                    "arquivo": instance.search(0)["nome_do_arquivo"],
                    "ocorrencias": occurrencies,
                }
            )
            return word_occurrencies
        else:
            return word_occurrencies


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
