def exists_word(word, instance):
    line = 0
    result = []
    for element in instance.data:
        search = {
            "palavra": word,
            "arquivo": element['nome_do_arquivo'],
            "ocorrencias": []
        }
        for phrase in element["linhas_do_arquivo"]:
            if word.lower() in phrase.lower():
                line += 1
                search["ocorrencias"].append({"linha": line})
        if len(search["ocorrencias"]) > 0:
            result.append(search)

    return result


def search_by_word(word, instance):
    line = 0
    result = []
    for element in instance.data:
        search = {
            "palavra": word,
            "arquivo": element['nome_do_arquivo'],
            "ocorrencias": []
        }
        for phrase in element["linhas_do_arquivo"]:
            if word.lower() in phrase.lower():
                line += 1
                search["ocorrencias"].append({
                    "linha": line,
                    "conteudo": phrase
                })
        if len(search["ocorrencias"]) > 0:
            result.append(search)

    return result
