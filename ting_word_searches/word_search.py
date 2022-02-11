def exists_word(word, instance):
    for i in range(instance.__len__()):
        data_file = instance.search(i)
        data = {
            'palavra': word,
            'arquivo': data_file['nome_do_arquivo'],
            'ocorrencias': []
        }
        i = 0
        for line in data_file['linhas_do_arquivo']:
            i += 1
            if word in line:
                data['ocorrencias'].append({'linha': i})
        if (len(data['ocorrencias']) <= 0):
            return []
        return [data]


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
