def exists_word(word, instance):
    for index in range(instance.__len__()):
        file_data = instance.search(index)
        data = {
            'palavra': word,
            'arquivo': file_data['nome_do_arquivo'],
            'ocorrencias': []
        }
        index = 0
        for line in file_data['linhas_do_arquivo']:
            index += 1
            if word in line:
                data['ocorrencias'].append({'linha': index})
        if (len(data['ocorrencias']) <= 0):
            return []
        return [data]


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
