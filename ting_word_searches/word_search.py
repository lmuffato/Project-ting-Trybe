def exists_word(word, instance):
    result = []

    for position in range(len(instance)):
        file = instance.search(position)

        data = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                data["ocorrencias"].append({"linha": index + 1})

        if len(data["ocorrencias"]):
            result.append(data)

    return result


def search_by_word(word, instance):
    result = []

    for position in range(len(instance)):
        file = instance.search(position)

        data = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                data["ocorrencias"].append(
                    {"linha": index + 1, "conteudo": line}
                )

        if len(data["ocorrencias"]):
            result.append(data)

    return result
