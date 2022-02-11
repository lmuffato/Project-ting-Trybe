def exists_word(word, instance):
    palavra = []
    content = instance.fila[0]
    print(content)
    for line in content["linhas_do_arquivo"]:
        if word in line:
            palavra.append(
                {"linha": content["linhas_do_arquivo"].index(line) + 1}
            )
    result = [{
        "palavra": word,
        "arquivo": content["nome_do_arquivo"],
        "ocorrencias": palavra,
    }]
    if result == []:
        return None
    print(result)
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
