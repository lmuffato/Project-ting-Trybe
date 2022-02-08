def exists_word(word, instance):
    list_index = []
    teste = []
    """result = [
        line for line in instance.fila["linhas_do_arquivo"] if word in line
    ]"""
    for line in instance.fila:

        if word in line["linhas_do_arquivo"]:
            teste.append(line)
        else:
            return teste
    for line in teste:
        index = instance.fila["linhas_do_arquivo"].index(line)
        list_index.append({"linha": index})
        return [
            {
                "palavra": word,
                "arquivo": instance.fila["nome_do_arquivo"],
                "ocorrencias": list_index,
            }
        ]


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
