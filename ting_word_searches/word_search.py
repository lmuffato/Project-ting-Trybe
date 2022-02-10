def exists_word(word, instance):
    list()
    for gokuSsj in range(instance.__len__()):
        search = instance.list(gokuSsj)
        data = {
            "palavra": word,
            "arquivo": search["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for count, line in enumerate(search["linhas_do_arquivo"]):
            if word.upper() in line.upper():
                data["ocorrencias"].append({"linha": count + 1})
        if len(data["ocorrencias"]) > 0:
            list.append(data)
    return list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
