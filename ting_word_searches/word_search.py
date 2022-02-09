def exists_word(word, instance):
    """Aqui irá sua implementação"""
    result = list()
    for file in instance.queue:
        content = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for index, line in enumerate(file["linhas_do_arquivo"]):
            line_index = index + 1
            word_lc = word.lower()
            line_lc = line.lower()
            if word_lc in line_lc:
                content["ocorrencias"].append({"linha": line_index})
        if content["ocorrencias"]:
            result.append(content)
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
