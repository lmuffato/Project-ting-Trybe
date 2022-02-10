from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    occurrences = []
    words_found_list = []

    for file in instance.queue:
        txt_file = txt_importer(file)
        index = 1
        while len(txt_file) >= index:
            if word.lower() in txt_file[index - 1].lower():
                occurrences.append({"linha": index})
            index += 1
        words_found_list.append(
            {"palavra": word, "arquivo": file, "ocorrencias": occurrences}
        )
    return [] if len(occurrences) == 0 else words_found_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
