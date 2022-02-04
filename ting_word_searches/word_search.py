from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    output = list()
    count = 0
    for path_files in instance.list:
        data = txt_importer(path_files)
        for phrase in data:
            if word in phrase:
                count += 1
                linha = [{"linha": count}]
                data_format = {
                    "palavra": word,
                    "arquivo": path_files,
                    "ocorrencias": linha
                }
                output.append(data_format)
    return output


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
