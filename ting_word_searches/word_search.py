from ting_file_management.file_process import process
from ting_file_management.queue import Queue


def exists_word(word, instance):
    """Aqui irá sua implementação"""
    response = list()
    lineIndex = 0

    for file in range(len(instance)):

        search = instance.search(file)

        searchResult = {
            "palavra": word,
            "arquivo": search["nome_do_arquivo"],
            "ocorrencias": []
        }

        for line in range(len(search["linhas_do_arquivo"])):
            if word.lower() in search["linhas_do_arquivo"][line].lower():
                lineIndex += 1
                searchResult["ocorrencias"].append({"linha": lineIndex})
            if len(searchResult["ocorrencias"]) > 0:
                response.append(searchResult)

    return response


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    response = list()
    lineIndex = 0

    for file in range(len(instance)):

        search = instance.search(file)

        searchResult = {
            "palavra": word,
            "arquivo": search["nome_do_arquivo"],
            "ocorrencias": []
        }

        for line in range(len(search["linhas_do_arquivo"])):
            if word.lower() in search["linhas_do_arquivo"][line].lower():
                lineIndex += 1
                searchResult["ocorrencias"].append({"linha": lineIndex, "conteudo": search["linhas_do_arquivo"][line]})
            if len(searchResult["ocorrencias"]) > 0:
                response.append(searchResult)

    return response
