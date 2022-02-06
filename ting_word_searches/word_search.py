def exists_word(word, instance):
    data_list = []
    ocurrencies = []
    print(instance._data)
    for text in instance._data:
        print(text)
        line_number = 0
        for line in text['linhas_do_arquivo']:
            line_number += 1
            if word in line:
                lineAndContent = {"linha": line_number}
                ocurrencies.append(lineAndContent)
        if len(ocurrencies) == 0:
            return ocurrencies
        text_data = {
            "palavra": word,
            "arquivo": text['nome_do_arquivo'],
            "ocorrencias": ocurrencies, }
        data_list.append(text_data)
    return data_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
