def exists_word(word, instance):
    return_list = []
    for file in instance.queue:
        lines = file['linhas_do_arquivo']
        add_dict = {
            'palavra': word,
            'arquivo': file['nome_do_arquivo'],
            'ocorrencias': [],
        }
        for index in range(len(lines)):
            if word.lower() in lines[index].lower():
                add_dict['ocorrencias'].append({'linha': index + 1})
        if len(add_dict['ocorrencias']) > 0:
            return_list.append(add_dict)
    return return_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
