import sys


def txt_importer(path_file):
    answer = []
    # https://www.w3schools.com/python/ref_string_endswith.asp
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file) as file:
            for line in file:
                answer.append(line.replace("\n", ""))
            return answer
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")


print(txt_importer('statics/arquivo_teste.txt'))
