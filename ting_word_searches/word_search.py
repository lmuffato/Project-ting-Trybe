import re


# Referência:
# https://github.com/tryber/sd-010-a-project-ting/pull/29/commits/fd505684f5436b6ae479cbe5b2881820e97492a8

def exists_word(word, instance):
    result = []

    for index in range(len(instance)):
        values = instance.search(index)
        ocurrences = []

        for key, line in enumerate(values["linhas_do_arquivo"]):
            # Regex:
            # https://pt.stackoverflow.com/questions/296286/encontrar-determinado-texto-em-uma-string
            phrase = re.search(word, line, re.IGNORECASE)
            # ----------------------------------------------------------------------------------------------
            if phrase:
                ocurrences.append({"linha": key + 1})

        if ocurrences:
            result.append({
             "arquivo": values["nome_do_arquivo"],
             "palavra": word,
             "ocorrencias": ocurrences
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
