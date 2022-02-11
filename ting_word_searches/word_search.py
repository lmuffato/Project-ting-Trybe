def exists_word(word, instance):
    """Aqui irá sua implementação"""
    for i in range(len(instance)):
        arquivo = instance.search(i)
        retorno_modelo = {
            "palavra": word,
            "arquivo": arquivo["nome_do_arquivo"],
            "ocorrencias": [],
        }
        atual_value = 0
        for index, line in enumerate(arquivo["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                retorno_modelo['ocorrencias'].append({
                    "linha": atual_value + 1
                })
                return [retorno_modelo]
            return []

# desafio realizado com pesquisa ao código do colega Eduardo Seije
# https://github.com/tryber/sd-010-a-project-ting/pull/58
# e consulta ao artigo https://www.codigofluente.com.br
# /listas-em-python/#:~:text=A%20fun%C3%A7%C3%A3o%20enumerate()
# %20retorna,um%20item%20da%20sequ%C3%AAncia%20correspondente.&text=
# lista%2C%20n%C3%A3o%20geram%20novas%20listas.
# para entender o funcionamento do enumerate


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
