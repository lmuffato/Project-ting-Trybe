def exists_word(word, instance):
    outputs = []
    files = len(instance)

    for index in range(files):
        actual_file = instance.search(index)
        lines = actual_file["linhas_do_arquivo"]

        output_return = {
            "palavra": word,
            "arquivo": actual_file["nome_do_arquivo"],
            "ocorrencias": []
        }

        for index_line in range(len(lines)):
            if word.lower() in lines[index_line].lower():
                output_return["ocorrencias"].append({
                    "linha": index_line + 1,
                })

        if len(output_return["ocorrencias"]):
            outputs.append(output_return)

    return outputs


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
