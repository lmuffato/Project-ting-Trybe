def exists_word(word, instance):
    outputs = []
    total_files = len(instance)

    for index in range(total_files):
        curr_file = instance.search(index)
        lines = curr_file["linhas_do_arquivo"]

        output = {
            "palavra": word,
            "arquivo": curr_file["nome_do_arquivo"],
            "ocorrencias": []
        }

        for lines_index in range(len(lines)):
            if word.lower() in lines[lines_index].lower():
                output["ocorrencias"].append({
                    "linha": lines_index + 1,
                })
        if len(output["ocorrencias"]) > 0:
            outputs.append(output)

    return outputs


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
