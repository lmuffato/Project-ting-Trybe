def file_lines(word, lines):
    lines_file = []

    for index in range(len(lines)):
        if word.capitalize() in lines[index]:
            lines_file.append(lines[index])
        if not len(lines_file):
            return []

    return lines_file


def exists_word(word, instance):
    word_occurrences = []

    for line in instance.queue_value:
        lines_file = file_lines(word, line["linhas_do_arquivo"])

        if not len(lines_file):
            return lines_file

        for line_name in lines_file:
            index_line = line["linhas_do_arquivo"].index(line_name) + 1
            word_occurrences.append({"linha": index_line})

        return [
            {
                "palavra": word,
                "arquivo": line["nome_do_arquivo"],
                "ocorrencias": word_occurrences,
            }
        ]


def search_by_word(word, instance):
    word_occurrences = []

    for line in instance.queue_value:
        lines_file = file_lines(word, line["linhas_do_arquivo"])

        if not len(lines_file):
            return lines_file

        for line_name in lines_file:
            index_line = line["linhas_do_arquivo"].index(line_name) + 1

            word_occurrences.append({
                "linha": index_line,
                "conteudo": line["linhas_do_arquivo"][index_line - 1]
            })

        return [
            {
                "palavra": word,
                "arquivo": line["nome_do_arquivo"],
                "ocorrencias": word_occurrences,
            }
        ]
