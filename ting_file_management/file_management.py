import sys


def txt_importer(path_file: str):
    try:
        assert path_file.split('.')[-1] == 'txt'
        data = open(path_file, mode='r', encoding='utf-8')
        parsed_data = []
        for line in data:
            parsed_data.append(line.rstrip('\n'))
        data.close()
        return parsed_data
    except AssertionError:
        print('Formato inválido', file=sys.stderr)
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
