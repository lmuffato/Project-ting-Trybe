def exists_word(word, instance):
    # Push aleatório para tentar cancelar o avaliador que
    # está rodando a mais de "Started 1d 13h 32m 4s ago"

    for index in range(len(instance)):
        # Busca em todas as instâncias pelo index
        buscar_txt = instance.search(index)

        # Esse dicionário serve de parâmetro do que e onde será buscado
        parametros = {
            "palavra": word,
            "arquivo": buscar_txt["nome_do_arquivo"],
            "ocorrencias": []}

        # Informa em quais instâncias a palavra aparece
        # Depende do processamento das informações mais abaixo
        detalhe_busca = []

        numero_da_linha = 0
        # O arquivo "file_process.py" tem a chave "linhas_do_arquivo"
        # na função "process". Todo arquivo da fila já foi processado!
        for index in buscar_txt["linhas_do_arquivo"]:
            # Readme: "A busca deve ser case insensitive" => ".lower()"
            if word.lower() in index.lower():
                numero_da_linha += 1
                parametros["ocorrencias"].append({"linha": numero_da_linha})
                # A chave "linha" (Acima) é pedido no readme.

        # Se encontrar a palavra desejada, "detalhe_busca" será populado.
        if len(parametros["ocorrencias"]) > 0:
            detalhe_busca.append(parametros)

    return detalhe_busca


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
