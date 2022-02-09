def exists_word(word, instance):
    """Aqui irá sua implementação"""
    for index in range(len(instance)):
        search_txt = instance.search(index)

        parameters = {
            "palavra": word,
            "arquivo": search_txt["nome_do_arquivo"],
            "ocorrencias": []}

        search_details = []
        row_number = 0

        for index in search_txt["linhas_do_arquivo"]:
            if word.lower() in index.lower():
                row_number += 1
                parameters["ocorrencias"].append({"linha": row_number})
        if len(parameters["ocorrencias"]) > 0:
            search_details.append(parameters)
    return search_details


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    found_word = []
    if (not word or word is None):
        return found_word
