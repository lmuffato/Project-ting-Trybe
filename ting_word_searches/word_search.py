def exists_word(word, instance):
    for index in range(len(instance)):
        search_txt = instance.search(index)

        params = {
            "palavra": word,
            "arquivo": search_txt["nome_do_arquivo"],
            "ocorrencias": []}

        search_detail = []

        numero_da_linha = 0

        for index in search_txt["linhas_do_arquivo"]:
            if word.lower() in index.lower():
                numero_da_linha += 1
                params["ocorrencias"].append({"linha": numero_da_linha})

        if len(params["ocorrencias"]) > 0:
            search_detail.append(params)

    return search_detail


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
