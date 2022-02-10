def exists_word(word, instance):
    is_exists = list()
    for index in range(instance.__len__()):
        result = instance.search(index)
        data = {
            "palavra": word,
            "arquivo": result["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for increment, line in enumerate(result["linhas_do_arquivo"]):
            if word.upper() in line.upper():
                data["ocorrencias"].append({"linha": increment + 1})
        if len(data["ocorrencias"]) > 0:
            is_exists.append(data)
    return is_exists


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
