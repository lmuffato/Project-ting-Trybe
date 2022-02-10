import sys


# endswith https://www.w3schools.com/python/ref_string_endswith.asp
# sys.stderr.write()
# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
# + https://www.youtube.com/watch?v=5za6eRdHjpw
# python split https://www.w3schools.com/python/ref_string_split.asp

def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido\n")
    # para retornar caso o formato seja inválido
    try:
        with open(path_file, mode="r") as f:
            data = f.read()
            return data.split("\n")
    # le o arquivo e usa split para adicionar linhas

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    # captura o erro e devolve personalizado
