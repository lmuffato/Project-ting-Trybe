def exists_word(word, instance):
    response_obj = []

    for item in range(0, len(instance)):
        data = instance.search(item)
        result = {
            "palavra": word,
            "arquivo": data["nome_do_arquivo"],
            "ocorrencias": []
        }

        for index, item in enumerate(data["linhas_do_arquivo"]):
            if word.lower() in item.lower():
                result["ocorrencias"].append({
                    "linha": index + 1
                })

        if len(result["ocorrencias"]):
            response_obj.append(result)

    return response_obj


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
