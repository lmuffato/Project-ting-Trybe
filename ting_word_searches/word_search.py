def exists_word(word, instance):
    for i in range(len(instance)):
        get_txt = instance.search(i)

        param = {
            "palavra": word,
            "arquivo": get_txt["nome_do_arquivo"],
            "ocorrencias": []}

        details = []
        line_num = 0

        for i in get_txt["linhas_do_arquivo"]:
            if word.lower() in i.lower():
                line_num += 1
                param["ocorrencias"].append({"linha": line_num})
        if len(param["ocorrencias"]) > 0:
            details.append(param)
    return details


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
