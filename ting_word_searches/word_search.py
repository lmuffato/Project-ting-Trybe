import re
import sys
from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    search_results = []
    for index in range(len(instance)):  # loop each file
        file_data = instance.search(index)
        file_results = {
            'palavra': word,
            'arquivo': file_data['nome_do_arquivo'],
            'ocorrencias': [],
        }
        for line in file_data['linhas_do_arquivo']:  # loop each line
            if re.search(word, line, re.IGNORECASE):
                line_index = file_data['linhas_do_arquivo'].index(line)
                file_results['ocorrencias'].append({'linha': line_index + 1})
        if len(file_results['ocorrencias']) != 0:
            search_results.append(file_results)
    print(search_results, file=sys.stdout)
    return search_results


def search_by_word(word, instance):
    search_results = []
    for index in range(len(instance)):  # loop each file
        file_data = instance.search(index)
        file_results = {
            'palavra': word,
            'arquivo': file_data['nome_do_arquivo'],
            'ocorrencias': [],
        }
        for line in file_data['linhas_do_arquivo']:  # loop each line
            if re.search(word, line, re.IGNORECASE):
                line_index = file_data['linhas_do_arquivo'].index(line)
                file_results['ocorrencias'].append({
                    'linha': line_index + 1,
                    'conteudo': line
                    })
        if len(file_results['ocorrencias']) != 0:
            search_results.append(file_results)
    print(search_results, file=sys.stdout)
    return search_results
