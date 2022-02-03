def exists_word(word, instance):
    word_ocurrences_list = list()
    for txt_file in instance.queue:
        data = {
            "palavra": word,
            "arquivo": txt_file["nome_do_arquivo"],
            "ocorrencias": []
        }
        word_ocurrences_list.append(data)
        for index, line in enumerate(txt_file["linhas_do_arquivo"]):
            current_line = index + 1
            word_lowercase = word.casefold()
            line_lowercase = line.casefold()
            if word_lowercase in line_lowercase:
                word_ocurrences_list[index]["ocorrencias"].append({
                    "linha": current_line
                })
                if len(word_ocurrences_list[index]["ocorrencias"]) > 0:
                    return word_ocurrences_list
        return list()


def search_by_word(word, instance):
    word_ocurrences_list = list()
    for txt_file in instance.queue:
        data = {
            "palavra": word,
            "arquivo": txt_file["nome_do_arquivo"],
            "ocorrencias": []
        }
        word_ocurrences_list.append(data)
        for index, line in enumerate(txt_file["linhas_do_arquivo"]):
            current_line = index + 1
            word_lowercase = word.casefold()
            line_lowercase = line.casefold()
            if word_lowercase in line_lowercase:
                word_ocurrences_list[index]["ocorrencias"].append({
                    "linha": current_line,
                    "conteudo": line
                })
                if len(word_ocurrences_list[index]["ocorrencias"]) > 0:
                    return word_ocurrences_list
        return list()

# Source:
# https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python
# https://realpython.com/python-enumerate/
