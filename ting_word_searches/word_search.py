import inspect
import re


def search_occurrences_in_file(word, file, caller_name):
    lines_occurrences = []
    for key, line in enumerate(file['linhas_do_arquivo']):
        text = re.search(word, line, re.IGNORECASE)
        if text:
            if(caller_name == 'exists_word'):
                lines_occurrences.append({"linha": key + 1})
            else:
                lines_occurrences.append({"linha": key + 1, "conteudo": line})
    return lines_occurrences


def get_occurrences(word, instance):
    occurrences = []
    # Source:
    # https://stackoverflow.com/questions/900392/getting-the-caller-function-name-inside-another-function-in-python/900404
    caller_name = inspect.stack()[1][3]

    for index in range(len(instance)):
        file = instance.search(index)
        lines_occurrences = search_occurrences_in_file(word, file, caller_name)
        if lines_occurrences:
            occurrences.append({
                "arquivo": file['nome_do_arquivo'],
                "palavra": word,
                "ocorrencias": lines_occurrences,
            })
    return occurrences


def exists_word(word, instance):
    occurrences = get_occurrences(word, instance)
    return occurrences


def search_by_word(word, instance):
    occurrences = get_occurrences(word, instance)
    return occurrences
