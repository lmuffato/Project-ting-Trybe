def exists_word(word, instance):
    occurences = list()
    for file in instance.get():
        matches = list()
        for index, line in enumerate(file['linhas_do_arquivo']):
            if line.lower().count(word.lower()) > 0:
                matches.append({'linha': index + 1})
        if len(matches) > 0:
            occurence = {
                'palavra': word,
                'arquivo': file,
                'ocorrencias': matches
            }
            occurences.append(occurence)
    return occurences


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
