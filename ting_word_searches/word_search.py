def exists_word(word, instance):
    word_exists = [
        {
            "palavra": word,
            "arquivo": txt_file["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for txt_file in instance.queueFifo
    ]

    for txt_file in instance.queueFifo:
        for index, line in enumerate(txt_file["linhas_do_arquivo"]):
            current_line = index + 1
            if word.lower() in line.lower():
                word_exists[index]["ocorrencias"].append(
                    {"linha": current_line}
                )
            if len(word_exists[index]["ocorrencias"]) > 0:
                return word_exists
        return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
