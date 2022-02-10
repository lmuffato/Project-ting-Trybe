def exists_word(word, instance):
    """Aqui irá sua implementação"""
    result = list()
    for file in instance.values:
        content = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for index, line in enumerate(file["linhas_do_arquivo"]):
            line_index = index + 1
            word_to_find = word.lower()
            line_to_search = line.lower()
            if word_to_find in line_to_search:
                content["ocorrencias"].append({"linha": line_index})
        if content["ocorrencias"]:
            result.append(content)
    return result

# Src: código feito com base no código apresentado pelo amigo Robertson
# https://github.com/tryber/sd-010-a-project-ting/pull/71/files


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
