from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    results = []
    line_counter = 0
    files = instance.head_value
    for file in files:
        phrase_for_row = txt_importer(file)
        for phrase in phrase_for_row:
            line_counter += 1
            if (word in phrase):
                add_file = {
                    "palavra": word,
                    "arquivo": file,
                    "ocorrencias": [{"linha": line_counter}]
                    }
                results.append(add_file)
    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
