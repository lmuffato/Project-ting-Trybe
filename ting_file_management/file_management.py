import sys


def txt_importer(path_file):
    try:
        if path_file.endswith(".txt"):
            with open(path_file, "r") as file:
                text = file.readlines()
                array_texts = []

                for line in text:
                    # https://www.w3schools.com/python/ref_string_rstrip.asp
                    array_texts.append(line.rstrip("\n"))
                    # -------------------------------------------------------
                return array_texts
        else:
            # https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
            print("Formato inválido", file=sys.stderr)

    # https://www.delftstack.com/pt/howto/python/how-to-check-if-a-file-exists-in-python/
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
