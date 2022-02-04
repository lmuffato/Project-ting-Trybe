def exists_word(word, instance):
    """Aqui irá sua implementação"""
    file = instance.dequeue()
    result = []
    lower_case_word = word.lower()

    for index, line in enumerate(file["linhas_do_arquivo"]):
        lower_case_line = line.lower()
        if lower_case_word in lower_case_line:
            result.append({"linha": index + 1})

    if not len(result):
        return result

    return [
        {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": result,
        }
    ]


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
