def get_files_name(queue):
    files_names = []
    for msg in queue.__queue__():
        files_names.append(msg["nome_do_arquivo"])
    return files_names
