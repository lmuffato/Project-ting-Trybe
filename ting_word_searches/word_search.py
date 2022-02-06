def exists_word(word, instance):
    words_qty = list()
    for file in instance.items:
        data = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": []
        }
        words_qty.append(data)
        for index, line in enumerate(file["linhas_do_arquivo"]):
            current_line = index + 1
            if word.lower() in line.lower():
                words_qty[index]["ocorrencias"].append({
                    "linha": current_line
                })
                if len(words_qty[index]["ocorrencias"]) > 0:
                    return words_qty
        return list()


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
