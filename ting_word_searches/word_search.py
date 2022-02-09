def exists_word(word, instance):
    processed_files_list = []

    for index in range(len(instance)):
        file_content = instance.search(index)

        file_name = file_content["nome_do_arquivo"]

        file_lines = file_content["linhas_do_arquivo"]

        process_lines = []

        for line in file_lines:
            if word.lower() in line:
                process_lines.append(
                    {{"linha": file_lines.index(line), "conteudo": line}}
                )

        if len(process_lines) == 0:
            return []

        processed_files_list.append(
            {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": process_lines,
            }
        )

    return processed_files_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
