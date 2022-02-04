from ting_file_management.file_management import txt_importer
# from ting_file_management.queue import Queue


def exists_word(word, instance):
    occurrence = []
    response = []

    for path in instance.list_ting:
        list_file = txt_importer(path)
        position = 1
        while len(list_file) >= position:
            if word.lower() in list_file[position - 1].lower():
                occurrence.append({"linha": position})
            position += 1
        response.append({
            "palavra": word,
            "arquivo": path,
            "ocorrencias": occurrence,
        })

    return [] if len(occurrence) == 0 else response


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


# test = Queue()
# test.enqueue("statics/arquivo.txt")
# print(exists_word("de", test))
