def exists_word(word, instance):
    found_ocurrences = []
    for file in instance.queue:
        found_ocurrences.append({
            "palavra": word,
            "arquivo": file['nome_do_arquivo'],
            "ocorrencias": []
        })
        for index, line in enumerate(file['linhas_do_arquivo']):
            if word in line:
                found_ocurrences[-1]['ocorrencias'].append({
                    "linha": index + 1
                })

    return list(filter(lambda x: len(x['ocorrencias']) > 0, found_ocurrences))


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
