def exists_word(word, instance):
    """Aqui irá sua implementação"""
    word_found = list()
    for txt_file in instance.items:
        data = {
            "palavra": word,
            "arquivo": txt_file["nome_do_arquivo"],
            "ocorrencias": []
        }
        word_found.append(data)
        for index, line in enumerate(txt_file["linhas_do_arquivo"]):
            current_line = index + 1
            if word.lower() in line.lower():
                word_found[index]["ocorrencias"].append({
                    "linha": current_line
                })
                if len(word_found[index]["ocorrencias"]) > 0:
                    return word_found
        return list()


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
