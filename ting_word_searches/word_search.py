def exists_word(word: str, instance):
    words_qty = list()
    for single_file in instance.data:
        data = {
            "palavra": word,
            "arquivo": single_file["nome_do_arquivo"],
            "ocorrencias": []
        }
        words_qty.append(data)
        for index, line in enumerate(single_file["linhas_do_arquivo"]):
            line_index = index + 1
            if word.casefold() in line.casefold():
                words_qty[index]["ocorrencias"].append({
                    "linha": line_index
                })
                if len(words_qty[index]["ocorrencias"]) > 0:
                    return words_qty
        return list()


def search_by_word(word, instance):
    """Aqui irá sua implementação"""