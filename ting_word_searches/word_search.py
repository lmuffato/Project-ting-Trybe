from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    ocurrences = list()
    count = 0
    for path_file in instance.list:
        data = txt_importer(path_file)
        for line in data:
            if word in line:
                count += 1
                linha = [{"linha": count}]
                formated_data = {
                    "palavra": word,
                    "arquivo": path_file,
                    "ocorrencias": linha
                }
                ocurrences.append(formated_data)
    return ocurrences


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
