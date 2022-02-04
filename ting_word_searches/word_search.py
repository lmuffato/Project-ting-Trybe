from ting_file_management.file_management import txt_importer
# from ting_file_management.queue import Queue


def exists_word(word, instance):
    return search(word, instance, False)


def search_by_word(word, instance):
    return search(word, instance, True)


def search(word, instance, is_search):
    occurrence = []
    response = []

    for path in instance.list_ting:
        list_file = txt_importer(path)
        position = 1
        while len(list_file) >= position:
            index = position - 1
            if word.lower() in list_file[index].lower():
                occurrence.append({"linha": position})
                if is_search:
                    occurrence[index]["conteudo"] = list_file[index]
            position += 1
        response.append({
            "palavra": word,
            "arquivo": path,
            "ocorrencias": occurrence,
        })

    return [] if len(occurrence) == 0 else response


# test = Queue()
# test.enqueue("statics/arquivo.txt")
# print(exists_word("de", test))
