def exists_word(word, instance):
    data = []

    for item in instance.list:
        acc = []
        data.append({
            'palavra': word,
            'arquivo': item['nome_do_arquivo'],
            'ocorrencias': acc
        })

        for index, line in enumerate(item['linhas_do_arquivo']):
            if word in line:
                acc.append({
                    'linha': index + 1
                })
        if not len(acc):
            data.pop()

    return data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
