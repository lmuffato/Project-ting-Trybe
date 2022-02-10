def exists_word(word, instance):
    # """Aqui irá sua implementação"""
    # Ref: Rep. Nathalia Zebral. Link:
    # https://github.com/tryber/sd-010-a-project-ting/pull/64/files

    # Valores retornados em forma de lista, como pede o requisito
    returned_list = list()
    # itera todos os elementos da fila
    for index in range(len(instance)):
        # usa uma função da classe queue para buscar um dos textos...
        # armazenados, pelo índice que é iterado.
        text = instance.search(index)

    # formata o padrão de data a ser retornado, conforme mostrado no readme
        data = {
            "palavra": word,
            "arquivo": text["nome_do_arquivo"],
            "ocorrencias": []
        }

        # Variável auxiliar para armazenar a linha que está sendo iterada...
        # e que contem a ocorrencia da palavra.
        line = 0

        # Iteração do sobre o texto de cada elemento...
        # armazenado pela classe queue
        for element in text["linhas_do_arquivo"]:
            # as palavras precisam estar em case insensitive e...
            # a palavra vindo do parâmetro
            # precisa corresponder ao texto iterado para gerar uma ocorrencia
            if word.lower() in element.lower():
                # Aumenta as linhas até encontrar uma ocorrencia
                line += 1
                # Altera a variavel data para acrescentar
                # na chave ocorrencias a linha encontrada
                data["ocorrencias"].append({
                    "linha": line
                })
        # Se existe uma palavra que corresponde...
        # a busca, uma lista correspondente aos...
        # itens retornados deve ser devolvida.
        # Caso nenhum item seja encontrado, a lista
        # por padrao continua vazia.
        if len(data["ocorrencias"]) > 0:
            # Adiciona data à lista retornada.
            returned_list.append(data)

    return returned_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
