def exists_word(word, instance):
    return get_ocurrencies(word, instance)


def search_by_word(word, instance):
    return get_ocurrencies(word, instance, True)


def get_ocurrencies(word, instance, hasContent=False):
    ocurrencies = [
        parse_node(node, word, hasContent)
        for node in instance.queue
    ]

    return [
        ocurrencie
        for ocurrencie in ocurrencies
        if len(ocurrencie["ocorrencias"]) > 0
    ]


def parse_node(node, word, hasContent):
    return {
        "palavra": word,
        "arquivo": node["nome_do_arquivo"],
        "ocorrencias": parse_ocurrencies(
            node["linhas_do_arquivo"],
            word,
            hasContent
        )
    }


def parse_ocurrencies(txt, word, hasContent):
    return [
        parse_line(line, index + 1, hasContent)
        for index, line in enumerate(txt)
        if word.casefold() in line.casefold()
    ]


def parse_line(line, line_position, hasContent):
    if hasContent:
        return {
            "linha": line_position,
            "conteudo": line
        }

    return {
        "linha": line_position
    }
