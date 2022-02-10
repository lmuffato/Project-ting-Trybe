def exists_word(word, instance):
    for index in range(len(instance)):
        queueItem = instance.search(index)
    data = {
        "palavra": word,
        "arquivo": queueItem["nome_do_arquivo"],
        "ocorrencias": []
    }
    line = 0
    for index in queueItem["nome_do_arquivo"]:
        if word.lower() in index.lower():
            line += 1
            data["ocorrencias"].append({
                "linha": line
            })
    items = list()
    if len(data["ocorrencias"]) > 0:
        items.append(data)
    return items


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
