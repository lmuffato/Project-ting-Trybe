import re


def get_files_name(queue):
    files_names = []
    for msg in queue.__queue__():
        files_names.append(msg["nome_do_arquivo"])
    return files_names


def exists_word_in_msg(word, line):
    """
    https://www.w3schools.com/python/python_regex.asp
    https://www.w3schools.com/python/python_regex.asp#matchobject
    https://stackoverflow.com/questions/500864/case-insensitive-regular-expression-without-re-compile
    https://gitanswer.com/flake8-g-incorrectly-flagged-as-invalid-escape-sequence-replacement-issue-python-849566460
    https://www.pythontutorial.net/python-basics/python-raw-strings/
    """
    match_obj = re.search(r'{word}\s'.format(word=word), line, re.IGNORECASE)
    if match_obj is None:
        return False
    return True
