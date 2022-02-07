def get_files_name(queue):
    files_names = []
    for msg in queue:
        files_names.append(msg[0])
    return files_names
