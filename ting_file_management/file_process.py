from ting_file_management.file_management import txt_importer
import sys


# Informado no plantão que o parâmetro "instance"
# recebe as funcionalidades de Queue

def process(path_file, instance):
    # Verificação para ignorar arquivos com o mesmo nome
    for index in range(len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return None

    # Validações e leitura do TXT baseado na função "txt_importer"
    importar_txt = txt_importer(path_file)

    # Formata as informações de acordo com o Readme
    txt_processado = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(importar_txt),
        'linhas_do_arquivo': importar_txt
    }

    # Coloca a nova instância (Arquivo processado) na fila
    instance.enqueue(txt_processado)

    # Reademe pede que cada saída seja enviada pelo stdout
    # Referência de uso do stdout:
    # https://www.geeksforgeeks.org/sys-stdout-write-in-python
    sys.stdout.write(str(txt_processado))


def remove(instance):
    # Lembrete: IF precisa de um return para parar a execução do código!
    if not instance:
        return sys.stdout.write("Não há elementos\n")
        # O "\n" acima está somente no teste, não no readme!

    # Tirar da fila o arquivo especificado pela chave "nome_do_arquivo"
    tirar_da_fila = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {tirar_da_fila} removido com sucesso\n")
    # Acima não é necessário return porque não há nada mais
    # a ser executado, acabou a função de remover da fila!


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
