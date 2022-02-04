def txt_importer(path_file):
    content_file = []

    with open(path_file, mode="r") as file:
        text_content = [line.rstrip('\n') for line in file]

        content_file = text_content
        file.close()

    return content_file

# Conseguir extrair as linhas sem os espaços com a explicação:
# https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
