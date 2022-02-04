def exists_word(word, instance):
    word_list = list()

    for item in range(len(instance)):
        file = instance.search(item)

        word_object = {
          "palavra": word,
          "arquivo": file["nome_do_arquivo"],
          "ocorrencias": [],
        }

        for element_lines in file["linhas_do_arquivo"]:
            line_position = 0

            if word in element_lines:
                line_position += 1
                word_object["ocorrencias"].append({"linha": line_position})

        if len(word_object["ocorrencias"]) == 0:
            return list()

        word_list.append(word_object)

    return word_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
