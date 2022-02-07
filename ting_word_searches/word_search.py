from ting_file_management.util import exists_word_dto


def exists_word(word, instance):
    return_list = []
    curr_queue = instance.__queue__()
    for msg in curr_queue:
        return_list.append(exists_word_dto(word, msg))
    return return_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
