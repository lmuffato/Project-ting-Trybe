import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file not in instance.queue:
        txt_file = txt_importer(path_file)
        instance.enqueue(path_file)
        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(txt_file),
            "linhas_do_arquivo": txt_file
        }
        return sys.stdout.write(f"{data}")


def remove(instance):
    if not instance:
        return sys.stdout.write("Não há elementos\n")
    else:
        txt_file = instance.dequeue()
        return sys.stdout.write(f"Arquivo {txt_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        txt_file = instance.search(position)
        info = txt_importer(txt_file)
        data = {
            "nome_do_arquivo": txt_file,
            "qtd_linhas": len(info),
            "linhas_do_arquivo": info
        }
        sys.stdout.write(str(data))
    except IndexError:
        sys.stderr.write('Posição inválida')
