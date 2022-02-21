from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    # instance é uma instânica da fila retornada pela lista()
    # função que importa o texto
    for index in range(len(instance)):
        # se o arquivo tive ro mesmo nome, retorna nada
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    # dados do arquivo
    file = txt_importer(path_file)
    data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": (file),
        }
    # carrega uma instânica de enqueue com os dados
    instance.enqueue(data)
    # É necessário sempre transformar em string
    sys.stdout.write(str(data))  # imprimir no terminal
    return data  # apenas pra testar

# TESTE MANUAL
# from ting_file_management.queue import Queue
# project = Queue()
# print(process("statics/arquivo_teste.txt", project))


def remove(instance):
    # se não existir instância de queue ou se o
    # comprimento do objeto for igual a 0
    if not instance or instance.__len__() == 0:
        # retorna a mensagem no terminal
        return sys.stdout.write("Não há elementos\n")
    file_to_delete = instance.dequeue()
    # caminho do arquivo na propriedade "nome_do_arquivo"
    file_path = file_to_delete["nome_do_arquivo"]
    # mensagem retornada no terminal
    sys.stdout.write(f"Arquivo {file_path} removido com sucesso\n")


# TESTE MANUAL
# from ting_file_management.queue import Queue
# project = Queue()
# process("statics/arquivo_teste.txt", project)
# remove(project)  # Arquivo statics/arquivo_teste.txt removido com sucesso
# remove(project)  # Não há elementos


def file_metadata(instance, position):
    try:
        # procura o objeto pelo indice
        data_info = instance.search(position)
        # imprime no terminal as informações do elemento
        sys.stdout.write(str(data_info))
        return str(data_info)
    # no caso do indice não existir
    except IndexError:
        # retorna no terminal
        sys.stderr.write("Posição inválida")


# TESTE MANUAL
# from ting_file_management.queue import Queue
# project = Queue()
# process("statics/arquivo_teste.txt", project)
# print(file_metadata(project, 200))  # posição inválida


# teste automatizado
# python3 -m pytest tests/test_file_process.py
