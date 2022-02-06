def txt_importer(path_file):
    with open(path_file, 'r') as file:
        text_list = file.read().splitlines()
    return text_list
