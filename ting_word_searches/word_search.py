# Requisito 6

# https://qastack.com.br/programming/4940032/how-to-search-for-a-string-in-text-files


def exists_word(word, instance):
    # Instanicia funções do arquivo queue.py
    for index in range(instance.__len__()):

        search_data = instance.search(index)
        result = {
            "palavra": word,
            "arquivo": search_data["nome_do_arquivo"],
            "ocorrencias": [],
        }
        index = 0

        for line in search_data["linhas_do_arquivo"]:
            index += 1
            # Salva as linhas de ocorrencia da palavra
            if word in line:
                result["ocorrencias"].append({"linha": index})

            # Se não houver ocorrencia da palavra
            #  no arquivo deve se retorna vazio
        if len(result["ocorrencias"]) <= 0:
            return []
        return [result]


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
