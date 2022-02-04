# from ting_file_management.file_process import process
# from ting_file_management.queue import Queue


def exists_word(word, instance):
    for index in range(instance.__len__()):
        file_data = instance.search(index)
        data = {
            'palavra': word,
            'arquivo': file_data['nome_do_arquivo'],
            'ocorrencias': []
        }
        index = 0
        for line in file_data['linhas_do_arquivo']:
            index += 1
            if word in line:
                data['ocorrencias'].append({'linha': index})
        return [data]


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


# project = Queue()
# process('statics/nome_pedro.txt', project)
# word = exists_word('Pedro', project)
# print(word)
