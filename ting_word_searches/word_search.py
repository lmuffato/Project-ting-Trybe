# Para o desenvolvimento desta função, estudei um pouco do código
# do Vinicius Rodrigues presente na PR abaixo:
# https://github.com/tryber/sd-010-a-project-ting/pull/78

def exists_word(word, instance):
    for row in range(len(instance)):
        details = []
        row_number = 0
        search = instance.search(row)
        data = {
            "palavra": word,
            "arquivo": search['nome_do_arquivo'],
            "ocorrencias": []
        }

        for match in search['linhas_do_arquivo']:
            if word.lower() in match.lower():
                row_number += 1
                data["ocorrencias"].append({"linha": row_number})
        if len(data["ocorrencias"]) > 0:
            details.append(data)
    return details


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
