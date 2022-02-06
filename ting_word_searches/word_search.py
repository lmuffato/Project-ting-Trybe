def exists_word(word, instance):
    result = []
    for i in range(instance.__len__()):
        item = instance.search(i)
        dictio = {
            'palavra': word,
            'arquivo': item['nome_do_arquivo'],
            'ocorrencias': []
        }
        for index in range(item['qtd_linhas']):
            if word.lower() in item['linhas_do_arquivo'][index].lower():
                dictio['ocorrencias'].append({'linha': index + 1})
        if len(dictio['ocorrencias']) > 0:
            result.append(dictio)
    return result


def search_by_word(word, instance):
    result = []
    for i in range(instance.__len__()):
        item = instance.search(i)
        dictio = {
            'palavra': word,
            'arquivo': item['nome_do_arquivo'],
            'ocorrencias': []
        }
        for index in range(item['qtd_linhas']):
            if word.lower() in item['linhas_do_arquivo'][index].lower():
                dictio['ocorrencias'].append({
                    'linha': index + 1,
                    'conteudo': item['linhas_do_arquivo'][index]
                })
        if len(dictio['ocorrencias']) > 0:
            result.append(dictio)
    return result
