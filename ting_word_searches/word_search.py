def exists_word(word, instance):
    for i in range(len(instance)):
        search_file = instance.search(i)

        params = {
            "palavra": word,
            "arquivo": search_file["nome_do_arquivo"],
            "ocorrencias": [],
        }

        search_details = []
        row_number = 0

        for i in search_file["linhas_do_arquivo"]:
            if word.lower() in i.lower():
                row_number += 1
                params["ocorrencias"].append({"linha": row_number})
        if len(params["ocorrencias"]) > 0:
            search_details.append(params)
    return search_details


def search_by_word(word, instance):
    for i in range(len(instance)):
        search_file = instance.search(i)

        params = {
            "palavra": word,
            "arquivo": search_file["nome_do_arquivo"],
            "ocorrencias": [],
        }

        search_details = []
        row_number = 0

        for i in search_file["linhas_do_arquivo"]:
            if word.lower() in i.lower():
                row_number += 1
                params["ocorrencias"].append(
                    {"linha": row_number, "conteudo": i}
                )
        if len(params["ocorrencias"]) > 0:
            search_details.append(params)
    return search_details
