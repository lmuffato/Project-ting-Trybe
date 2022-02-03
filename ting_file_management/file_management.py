import csv
import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        return sys.stderr.write('Formato inválido\n')
    try:
        with open(path_file) as file:
            reader = csv.reader(file, delimiter="\n")
            rows = list()
            for row in reader:
                rows.append(row[0])
            return rows
    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
