# retorno esperado:
# [{
#  "palavra": "de",
#  "arquivo": "arquivo_teste.txt",
#  "ocorrencias": [
#    {
#      "linha": 1
#    },
#    {
#      "linha": 2
#    }
#  ]
# }]


def exists_word(word, instance):
    returnList = []

    for item in instance.data:
        events = []
        returnList.append({
            'palavra': word,
            'arquivo': item['nome_do_arquivo'],
            'ocorrencias': events
        })
        # Fonte: https://realpython.com/python-enumerate/
        for i, line in enumerate(item['linhas_do_arquivo']):
            if word in line:
                events.append({
                    'linha': i + 1
                })
        if not len(events):
            returnList.pop()

    return returnList


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
