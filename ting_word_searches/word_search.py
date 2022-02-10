def exists_word(word, instance):
    li = list()
    for gokuSsj in range(instance.__len__()):
        search = instance.search(
            gokuSsj
        )  # https://pythonexamples.org/python-re-search/
        data = {
            "palavra": word,
            "arquivo": search["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for count, line in enumerate(search["linhas_do_arquivo"]):
            if word.upper() in line.upper():
                data["ocorrencias"].append({"linha": count + 1})
        if len(data["ocorrencias"]) > 0:
            li.append(data)
    return li


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
