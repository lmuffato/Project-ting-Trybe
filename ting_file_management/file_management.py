def txt_importer(path_file):
    with open(path_file, "r") as file:
        return list(file.read().splitlines())
