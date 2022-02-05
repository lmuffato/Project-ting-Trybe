#  https://realpython.com/python-enumerate/


def exists_word(word, instance):
    result = list()
    for index in range(instance.__len__()):
        current = instance.search(index)
        data = {
            'palavra': word,
            'arquivo': current['nome_do_arquivo'],
            'ocorrencias': []
        }
        for count, line in enumerate(current['linhas_do_arquivo']):
            if word.upper() in line.upper():
                data['ocorrencias'].append({
                    'linha': count + 1
                })
        if len(data['ocorrencias']) > 0:
            result.append(data)
    return result


def search_by_word(word, instance):
    result = list()
    for index in range(instance.__len__()):
        current = instance.search(index)
        data = {
            'palavra': word,
            'arquivo': current['nome_do_arquivo'],
            'ocorrencias': []
        }
        for count, line in enumerate(current['linhas_do_arquivo']):
            if word.upper() in line.upper():
                data['ocorrencias'].append({
                    'linha': count + 1,
                    'conteudo': line
                })
        if len(data['ocorrencias']) > 0:
            result.append(data)
    return result
