def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return sys.stderr.write('Formato inválido\n')
    try:
        file = open(path_file, "r")
        # https://www.w3schools.com/python/ref_string_splitlines.asp
        splitedText = file.read().splitlines()
        return splitedText
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
