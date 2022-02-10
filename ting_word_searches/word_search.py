def exists_word(word, instance):
    itens = list()
    for i in range(instance.__len__()):
        readFile = instance.search(i)
        occurrences = list()
        for line, phrase in enumerate(readFile['linhas_do_arquivo'], start=1):
            if word in phrase:
                occurrences.append({'linha': line})
        if len(occurrences):
            itens.append({
                'palavra': word,
                'arquivo': readFile['nome_do_arquivo'],
                'ocorrencias': occurrences
            })
    return itens


def search_by_word(word, instance):
    itens = list()
    for i in range(instance.__len__()):
        readFile = instance.search(i)
        occurrences = list()
        for line, phrase in enumerate(readFile['linhas_do_arquivo'], start=1):
            if word.upper() in phrase.upper():
                occurrences.append({
                    'linha': line,
                    'conteudo': phrase
                })
        if len(occurrences):
            itens.append({
                'palavra': word,
                'arquivo': readFile['nome_do_arquivo'],
                'ocorrencias': occurrences
            })
    return itens
