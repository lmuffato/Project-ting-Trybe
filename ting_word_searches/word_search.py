from ting_file_management.file_process import txt_importer


def exists_word(word, instance):
    output = list()
    word_not_found = True
    for path_file in instance.list:
        word_report = {
            "palavra": word,
            "arquivo": path_file,
            "ocorrencias": list()
        }
        txt = txt_importer(path_file)
        line = 1
        for row in txt:
            if word.lower() in row.lower():
                word_not_found = False
                word_report['ocorrencias'].append({
                    "linha": line
                })
            line += 1
        output.append(word_report)
        if word_not_found:
            return list()
        return output


def search_by_word(word, instance):
    output = list()
    word_not_found = True
    for path_file in instance.list:
        word_report = {
            "palavra": word,
            "arquivo": path_file,
            "ocorrencias": list()
        }
        txt = txt_importer(path_file)
        line = 1
        for row in txt:
            if word.lower() in row.lower():
                word_not_found = False
                word_report['ocorrencias'].append({
                    "linha": line,
                    "conteudo": row
                })
            line += 1
        output.append(word_report)
        if word_not_found:
            return list()
        return output
