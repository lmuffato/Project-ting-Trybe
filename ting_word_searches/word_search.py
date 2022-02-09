def exists_word(word, instance):
    palavras_encontradas = []
    for txt_file in instance.items:
        data = {
            "palavra": word,
            "arquivo": txt_file["nome_do_arquivo"],
            "ocorrencias": []
        }
        palavras_encontradas.append(data)

    # https://realpython.com/python-enumerate/#unpacking-arguments-with-enumerate
        for index, line in enumerate(txt_file["linhas_do_arquivo"]):
            current_line = index + 1
            if word.lower() in line.lower():
                palavras_encontradas[index]["ocorrencias"].append({
                    "linha": current_line
                })
                if len(palavras_encontradas[index]["ocorrencias"]) > 0:
                    return palavras_encontradas
        return list()


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
