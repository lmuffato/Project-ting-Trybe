def exists_word(word, instance):
    filter_word = []
    data = instance.search(0)
    line = list(data["linhas_do_arquivo"])

    filter_word = list(filter(lambda el: word in el, line))
    if len(filter_word) == 0:
        return []
    return filter_word


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
