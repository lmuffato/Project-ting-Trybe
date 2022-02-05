
def exists_word(word: str, instance):
    words = list()
    for file in instance.data:
        data = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": []
        }
        words.append(data)
        # https://book.pythontips.com/en/latest/enumerate.html
        for index, line in enumerate(file["linhas_do_arquivo"]):
            current_line = index + 1
            word_lowercase = word.casefold()
            line_lowercase = line.casefold()
            if word_lowercase in line_lowercase:
                words[index]["ocorrencias"].append({
                    "linha": current_line
                })
                if len(words[index]["ocorrencias"]) > 0:
                    return words
        return list()


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
