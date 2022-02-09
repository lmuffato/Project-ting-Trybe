import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith(".txt"):
        # https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
        sys.stderr.write("Formato inválido\n")
        return None

    try:
        with open(path_file) as file:
            return [line.split("\n")[0] for line in file.readlines()]
    except FileNotFoundError:
        sys.stderr.write(
            "Arquivo statics/arquivo_nao_existe.txt não encontrado\n"
        )
        return None
