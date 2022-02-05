def exists_word(word, instance):
    searched = [{"palavra": word, "arquivo": "", "ocorrencias": []}]
    occurrences = []
    data = instance.data

    for item in data:
        searched[0]["arquivo"] = item["nome_do_arquivo"]
        lines = item["linhas_do_arquivo"]
        for index, line in enumerate(lines):
            if word.upper() in line.upper():
                occurrences.append({"linha": index + 1})
        searched[0]["ocorrencias"] = occurrences
        if len(occurrences) > 0:
            return searched
    return []


def search_by_word(word, instance):
    searched = [{"palavra": word, "arquivo": "", "ocorrencias": []}]
    occurrences = []
    data = instance.data

    for item in data:
        searched[0]["arquivo"] = item["nome_do_arquivo"]
        lines = item["linhas_do_arquivo"]
        for index, line in enumerate(lines):
            if word.upper() in line.upper():
                occurrences.append({"linha": index + 1, "conteudo": line})
        searched[0]["ocorrencias"] = occurrences
        if len(occurrences) > 0:
            return searched
    return []
