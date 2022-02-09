def exists_word(word, instance):
    found_words = []
    for entry in instance._data:
        result = {
            'palavra': word,
            'arquivo': entry['nome_do_arquivo'],
            'ocorrencias': []
        }

        for index, line in enumerate(entry['linhas_do_arquivo']):
            line = line.replace('.', '')
            if word.lower() in line.lower().split():
                result['ocorrencias'].append({'linha': index + 1})

        if len(result['ocorrencias']) > 0:
            found_words.append(result)

    return found_words


def search_by_word(word, instance):
    found_sentences = []
    for entry in instance._data:
        result = {
            'palavra': word,
            'arquivo': entry['nome_do_arquivo'],
            'ocorrencias': []
        }

        for index, line in enumerate(entry['linhas_do_arquivo']):
            line_minus_period = line.replace('.', '')
            if word.lower() in line_minus_period.lower().split():
                result['ocorrencias'].append({
                    'linha': index + 1,
                    'conteudo': line
                })

        if len(result['ocorrencias']) > 0:
            found_sentences.append(result)

    return found_sentences
