def exists_word(word, instance):
    """Aqui irá sua implementação"""
    info_file = []
    count = 0
    # primeiro, percorro os elementos da pilha
    for index in instance._data:
        info_return = {
            "palavra": word,
            "arquivo": index["nome_do_arquivo"],
            "ocorrencias": []
        }
    # segundo, percorro o texto
        for line in index["linhas_do_arquivo"]:
            if word in line:
                count += 1
                info_return["ocorrencias"].append({"linha": count})
        if len(info_return["ocorrencias"]) > 0:
            info_file.append(info_return)
    return info_file


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
