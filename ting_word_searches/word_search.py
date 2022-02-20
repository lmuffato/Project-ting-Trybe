def exists_word(word, instance):
    searchs = []
    size = len(instance)

    for n in range(size):
        info = instance.search(n)
        file, qtd_linhas, lines = info.values()
        msg = {
            'palavra': word,
            'arquivo': file,
            'ocorrencias': []
        }

        for n in range(qtd_linhas):
            line = lines[n]
            if word in line:
                msg['ocorrencias'].append({
                    'linha': n + 1,
                })
        if len(msg['ocorrencias']) > 0:
            searchs.append(msg)

    return searchs


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
