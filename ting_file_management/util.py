def get_files_name(queue):
    files_names = []
    for msg in queue:
        files_names.append(msg)
        print(files_names)
    return files_names
