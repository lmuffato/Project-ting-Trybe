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
    if not instance:
        return sys.stdout.write("Não há elementos\n")
    # se não ouver instance retorna messagem personalizada
    remove_file = instance.dequeue()["nome_do_arquivo"]
    # remove utilizando a func dequeue pelo nome do arquivo
    sys.stdout.write(f"Arquivo {remove_file} removido com sucesso\n")
    # confirma se foi removido


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
