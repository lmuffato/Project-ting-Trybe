def exists_word(word, instance):
    """Aqui irá sua implementação"""
    result = []
    for i in range(instance.__len__()):
        item = instance.search(i)
        the_dict = {
            'palavra': word,
            'arquivo': item['nome_do_arquivo'],
            'ocorrencias': []
        }
        for index in range(item['qtd_linhas']):
            if word.lower() in item['linhas_do_arquivo'][index].lower():
                the_dict['ocorrencias'].append({'linha': index + 1})
        if len(the_dict['ocorrencias']) > 0:
            result.append(the_dict)
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    result = []
    for i in range(instance.__len__()):
        item = instance.search(i)
        the_dict = {
            'palavra': word,
            'arquivo': item['nome_do_arquivo'],
            'ocorrencias': []
        }
        for index in range(item['qtd_linhas']):
            if word.lower() in item['linhas_do_arquivo'][index].lower():
                the_dict['ocorrencias'].append({
                    'linha': index + 1,
                    'conteudo': item['linhas_do_arquivo'][index]
                })
        if len(the_dict['ocorrencias']) > 0:
            result.append(the_dict)
    return result
