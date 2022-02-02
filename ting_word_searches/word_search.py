from ting_file_management.file_management import txt_importer


def search_type(word, file, type):
    found_word = list()
    index = 1
    for line in txt_importer(file):
        if word.lower() in line.lower():
            if type == "line":
                found_word.append({"linha": index})
            if type == "content":
                found_word.append({"linha": index, "conteudo": line})
        index += 1
    return found_word


def search(word, instance, type):
    return_list = list()
    for file in instance._list:
        found_word = search_type(word, file, type)
        if len(found_word) != 0:
            return_list.append(
                {"palavra": word, "arquivo": file, "ocorrencias": found_word}
            )
    return return_list


def exists_word(word, instance):
    return search(word, instance, 'line')


def search_by_word(word, instance):
    return search(word, instance, "content")
