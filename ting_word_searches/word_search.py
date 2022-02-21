def exists_word(word, instance):
    # array de ocorrências
    occurrences = []
    # para cada elemento na lista
    for element in instance.list:
        occurrences_lines = []  # linhas da ocorrência
        # informações da ocorrência
        occurrences.append({
            'palavra': word,
            'arquivo': element['nome_do_arquivo'],
            'ocorrencias': occurrences_lines
        })
        # Para cada índice e linha na lista criada pelo enumerate
        for index, line in enumerate(element['linhas_do_arquivo']):
            # A função enumerate cria uma lista de classe a partir de
            # um índice 0 ou determinado no segundo parâmetro opcional
            if word in line:  # se existir a palavra na linha
                # adiciona no array
                occurrences_lines.append({
                    'linha': index + 1
                })
        # se não tiver ocorrências
        if len(occurrences_lines) == 0:
            # remove e retorna o primeiro elemento da fila
            occurrences.pop()

    return occurrences


# TESTE MANUAL
# from ting_file_management.queue import Queue
# from ting_file_management.file_process import process
# project = Queue()
# process("statics/nome_pedro.txt", project)
# word = exists_word("Pedro", project)


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


# teste automatizado
# python3 -m pytest tests/test_word_search.py
