import re


def search_occurrences_in_file(word, file):
    lines_occurrences = []
    for key, line in enumerate(file['linhas_do_arquivo']):
        text = re.search(word, line, re.IGNORECASE)
        if text:
            lines_occurrences.append({"linha": key + 1})
    return lines_occurrences


def get_occurrences(word, instance):
    occurrences = []
    for index in range(len(instance)):
        file = instance.search(index)
        lines_occurrences = search_occurrences_in_file(word, file)
        if lines_occurrences:
            occurrences.append({
                "arquivo": file['nome_do_arquivo'],
                "palavra": word,
                "ocorrencias": lines_occurrences
            })
    return occurrences


def exists_word(word, instance):
    occurrences = get_occurrences(word, instance)
    return occurrences


def search_by_word(word, instance):
    pass
