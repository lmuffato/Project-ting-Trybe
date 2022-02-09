# https://pt.stackoverflow.com/questions/226182/quebra-de-linha-em-um-arquivo-txt
# o link acima serviu para ter conhecimento da função splitlines()

def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if path_file.endswith('.txt'):
        txt_file = open(path_file, "r").read().splitlines()
        return list(txt_file)
    else:
        print("Arquivo" + {path_file} + "não encontrado")
