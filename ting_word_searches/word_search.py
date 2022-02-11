def exists_word(word, instance):
    lineIndex = 0
    response = list()
    for file in range(len(instance)):
        searchResult = {
            "palavra": word,
            "arquivo": file['nome_do_arquivo'],
            "ocorrencias": []
        }
        for phrase in file["linhas_do_arquivo"]:
            if word.lower() in phrase.lower():
                lineIndex += 1
                searchResult["ocorrencias"].append({"linha": lineIndex})
        if len(searchResult["ocorrencias"]) > 0:
            response.append(searchResult)

    return response


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
