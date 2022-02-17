def exists_word(word, instance):
    """Aqui irá sua implementação"""
    data = []

    for index in range(len(instance)):
        file = instance.search(index)

        word_ocorruncy = {
          "palavra": word,
          "arquivo": file["nome_do_arquivo"],
          "ocorrencias": [],
        }

        for item in file["linhas_do_arquivo"]:
            line = 0

            if word in item:
                line += 1
                word_ocorruncy["ocorrencias"].append({"linha": line})

        if len(word_ocorruncy["ocorrencias"]) == 0:
            return []

        data.append(word_ocorruncy)

    return data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    data = []

    for index in range(len(instance)):
        file = instance.search(index)

        word_ocorruncy = {
          "palavra": word,
          "arquivo": file["nome_do_arquivo"],
          "ocorrencias": [],
        }

        for item in file["linhas_do_arquivo"]:
            line = 0

            if word in item:
                line += 1
                word_ocorruncy["ocorrencias"].append(
                    {"linha": line, "conteudo": item}
                )

        if len(word_ocorruncy["ocorrencias"]) == 0:
            return []

        data.append(word_ocorruncy)

    return data
