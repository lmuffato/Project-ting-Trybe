import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if instance.__len__() == 0:
        file = txt_importer(path_file)

        file_name = f"'nome_do_arquivo': '{path_file}'"
        lines_counter = f"'qtd_linhas': {len(file)}"
        lines = f"'linhas_do_arquivo': {file}"

        sys.stdout.write(f'{file_name}')
        sys.stdout.write(f'{lines_counter}')
        sys.stdout.write(f'{lines}')

        instance.enqueue(path_file)
    else:
        pass


def remove(instance):
    try:
        data = instance.dequeue()
        path_file = data['nome_do_arquivo']
        print(f'Arquivo {path_file} removido com sucesso\n', file=sys.stdout)
    except IndexError:
        sys.stdout.write(
            "Não há elementos\n"
        )


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        return sys.stdout.write(str(data))
    except IndexError:
        print("Posição inválida", file=sys.stderr)
