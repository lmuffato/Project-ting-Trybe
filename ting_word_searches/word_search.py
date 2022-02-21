def exists_word(word, instance):
    # Para cada elemento da lista
    for index in range(len(instance)):
        # elemento buscado pelo indice
        file = instance.search(index)
        # informações da pesquisa
        data_info = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }
        # linha de ocorrência
        linha = 0

        # Para cada elemento no conjunto de linhas
        for index in file["linhas_do_arquivo"]:
            # buscar a palavra em caixa baixa, no texto em caixa baixa
            if word.lower() in index.lower():
                linha += 1
                # adiciona no array de ocorrências
                data_info["ocorrencias"].append(
                  {
                    "linha": linha
                  }
                )

        search_info = []
        # se exisitir ocorrênica, adicionar ao array
        if len(data_info["ocorrencias"]) > 0:
            search_info.append(data_info)
    return search_info


# TESTE MANUAL
# from ting_file_management.queue import Queue
# from ting_file_management.file_process import process
# project = Queue()
# process("statics/nome_pedro.txt", project)
# word = exists_word("Pedro", project)


def search_by_word(word, instance):
    # para cada elemento da lista
    for index in range(len(instance)):
        # elemento buscado pelo indice
        file = instance.search(index)
        # informações
        data_info = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }

        linha = 0

        # Para cada elemento no conjunto de linhas
        for index in file["linhas_do_arquivo"]:
            # buscar a palavra em caixa baixa, no texto em caixa baixa
            if word.lower() in index.lower():
                linha += 1
                # adiciona no array de ocorrências
                data_info["ocorrencias"].append(
                    {
                      "linha": linha,
                      "conteudo": index,
                    }
                )

        search_info = []
        # se exisitir ocorrênica, adicionar ao array
        if len(data_info["ocorrencias"]) > 0:
            search_info.append(data_info)

    return search_info


# TESTE MANUAL
# from ting_file_management.queue import Queue
# from ting_file_management.file_process import process
# project = Queue()
# process("statics/nome_pedro.txt", project)
# print(search_by_word("pedro", project))

# teste automatizado
# python3 -m pytest tests/test_word_search.py
