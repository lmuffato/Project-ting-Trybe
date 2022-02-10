from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)['nome_do_arquivo'] == path_file:
            return None
    # ignora arquivos com mesmo nome
    text = txt_importer(path_file)
    # utiliza o func para formatar
    dataOut = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(text),
        'linhas_do_arquivo': text
    }
    # formata como dict
    instance.enqueue(dataOut)
    # adiciona na fila
    sys.stdout.write(str(dataOut))
    # escreve a saida no terminal (print)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
