from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    return search_response(word, instance, False)


def search_by_word(word, instance):
    return search_response(word, instance, True)


def search_response(word, instance, is_search):
    occurrence = []
    response = []

    for path in instance.list_ting:
        list_file = txt_importer(path)
        occurrence = get_search_occurrences(list_file, word, is_search)
        response.append({
            "palavra": word,
            "arquivo": path,
            "ocorrencias": occurrence,
        })

    return [] if len(occurrence) == 0 else response


def get_search_occurrences(list_file, word, is_search):
    occurrence = []
    position = 1

    while len(list_file) >= position:
        index = position - 1
        if word.lower() in list_file[index].lower():
            occurrence.append({"linha": position})
            if is_search:
                occurrence[index]["conteudo"] = list_file[index]
        position += 1

    return occurrence
