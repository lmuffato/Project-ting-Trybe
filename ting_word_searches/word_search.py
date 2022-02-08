def exists_word(word, instance):
    data = []
    for i in range(len(instance)):
        data.append({
            "palavra": word,
            "arquivo": "",
            "ocorrencias": [],
        })
        file = instance.search(i)
        for j, item in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in item.lower():
                data[i]["arquivo"] = file["nome_do_arquivo"]
                data[i]["ocorrencias"].append({"linha": j + 1})

    return [item for item in data if item["arquivo"] != ""]


def search_by_word(word, instance):
    data = []
    for i in range(len(instance)):
        data.append({
            "palavra": word,
            "arquivo": "",
            "ocorrencias": [],
        })
        file = instance.search(i)
        for j, item in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in item.lower():
                data[i]["arquivo"] = file["nome_do_arquivo"]
                data[i]["ocorrencias"].append({
                    "linha": j + 1,
                    "conteudo": item,
                    })

    return [item for item in data if item["arquivo"] != ""]
