import re


def exists_word(word, instance):
    result = []

    for index, file in enumerate(instance.data):
        obj = {
            'palavra': word,
            'arquivo': file['nome_do_arquivo'],
            'ocorrencias': []
        }

        [value] = file['linhas_do_arquivo']

        if re.search(word, value, re.IGNORECASE):
            ocurr = {
                'linha': index + 1
            }
            obj['ocorrencias'].append(ocurr)

        if len(obj['ocorrencias']) > 0:
            result.append(obj)

    return result


def search_by_word(word, instance):
    result = []

    for index, file in enumerate(instance.data):
        obj = {
            'palavra': word,
            'arquivo': file['nome_do_arquivo'],
            'ocorrencias': []
        }

        [value] = file['linhas_do_arquivo']

        if re.search(word, value, re.IGNORECASE):
            ocurr = {
                'linha': index + 1,
                'conteudo': value
            }
            obj['ocorrencias'].append(ocurr)

        if len(obj['ocorrencias']) > 0:
            result.append(obj)

    return result
