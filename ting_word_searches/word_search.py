from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    return_list = list()
    for file in instance._list:
        found_word = list()
        index = 1
        for line in txt_importer(file):
            if word.lower() in line.lower():
                found_word.append({"linha": index})
            index += 1
        if len(found_word) != 0:
            return_list.append(
                {"palavra": word, "arquivo": file, "ocorrencias": found_word}
            )
    return return_list


def search_by_word(word, instance):
    return_list = list()
    for file in instance._list:
        found_word = list()
        index = 1
        for line in txt_importer(file):
            if word.lower() in line.lower():
                found_word.append({"linha": index, "conteudo": line})
            index += 1
        if len(found_word) != 0:
            return_list.append(
                {"palavra": word, "arquivo": file, "ocorrencias": found_word}
            )
    return return_list
