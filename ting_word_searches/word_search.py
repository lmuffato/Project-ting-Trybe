def exists_word(word, instance):
    data_list = list()
    for index in instance.queue:
        line = index['linhas_do_arquivo']
        data = {
            'palavra': word,
            'arquivo': index['nome_do_arquivo'],
            'ocorrencias': [],
        }
        for index in range(len(line)):
            if word.upper() in line[index].upper():
                data['ocorrencias'].append({'linha': index + 1})
        if 0 < len(data['ocorrencias']):
            data_list.append(data)
    return data_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
