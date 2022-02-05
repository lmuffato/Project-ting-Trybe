from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    data = instance.search(0)
    text_file = txt_importer(instance.search(0))
    occur = []
    answer = [
        {
            "palavra": f"{word}",
            "arquivo": f"{data}",
            "ocorrencias": occur,
        }
    ]
    for index, row in enumerate(text_file):
        if word in row:
            occur.append({"linha": int(f"{index  + 1}")})
        if occur:
            return answer
    return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
