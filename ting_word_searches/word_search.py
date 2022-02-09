def exists_word(word, instance):
    seach = list()
    for index in range(instance.__len__()):
        data_seach = instance.search(index)
        data = {
            'palavra': word,
            'arquivo': data_seach['nome_do_arquivo'],
            'ocorrencias': []
        }
        for count, line in enumerate(data_seach['linhas_do_arquivo']):
            if word.upper() in line.upper():
                data['ocorrencias'].append({
                    'linha': count + 1
                })
        if len(data['ocorrencias']) > 0:
            seach.append(data)
    return seach


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
