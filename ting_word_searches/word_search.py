def exists_word(word, instance):
    report = []
    occurrences = 0
    for file in instance.queue:
        file_report = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [
                {"linha": index + 1}
                for index, linha in enumerate(file["linhas_do_arquivo"])
                if word.lower() in linha.lower()
            ],
        }
        occurrences += len(file_report["ocorrencias"])
        report.append(file_report)
    if not occurrences:
        report = []
    return report

def search_by_word(word, instance):
    report = []
    occurrences = 0
    for file in instance.queue:
        file_report = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [
                {"linha": index + 1, "conteudo": linha}
                for index, linha in enumerate(file["linhas_do_arquivo"])
                if word.lower() in linha.lower()
            ],
        }

        occurrences += len(file_report["ocorrencias"])
        report.append(file_report)
    if not occurrences:
        report = []
    return report