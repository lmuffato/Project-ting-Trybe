def exists_word(word, instance):
    result = []

    for data in instance.data:
        possible = []
        result.append({
            'palavra': word,
            'arquivo': data['nome_do_arquivo'],
            'ocorrencias': possible
        })
        for index, line in enumerate(data['linhas_do_arquivo']):
            if word in line:
                possible.append({'linha': index + 1})
        if not len(possible):
            result.pop()

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
