def exists_word(word, instance):
    for i in range(len(instance)):
        search = instance.search(i)
        # busca conteúdo pelo index
        params_d = {
            "palavra": word,
            "arquivo": search["nome_do_arquivo"],
            "ocorrencias": []}
        num = 0
        data = []
        for i in search["linhas_do_arquivo"]:
            if word.lower() in i.lower():
                num += 1
                params_d["ocorrencias"].append({"linha": num})
        if len(params_d["ocorrencias"]) > 0:
            data.append(params_d)
    return data
    # A busca deve ser case insensitive e deve retornar uma lista no formato:
    # lower https://www.w3schools.com/python/ref_string_lower.asp


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
