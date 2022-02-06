def exists_word(word, instance):
    data_list = list()
    for item in instance.data:
        data = {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": []
        }
        data_list.append(data)
        for index, line in enumerate(item["linhas_do_arquivo"]):
            current_line = index + 1
            if word.lower() in line.lower():
                data_list[index]["ocorrencias"].append({
                    "linha": current_line
                })
                if len(data_list[index]["ocorrencias"]) > 0:
                    return data_list
        return list()


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
