import sys

from black import Index
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer

def file_already_imported(path_file: str, instance: Queue) -> bool:
  is_path_imported = path_file in [x["nome_do_arquivo"] for x in instance.data]
  return is_path_imported

def process(path_file: str, instance: Queue):
    if file_already_imported(path_file, instance) is True:
      return

    lines = txt_importer(path_file)

    output = {}
    output["nome_do_arquivo"] = path_file
    output["qtd_linhas"] = len(lines)
    output["linhas_do_arquivo"] = lines

    instance.enqueue(output)
    print(output)

def remove(instance: Queue):
  if(len(instance) == 0):
    print('Não há elementos')
    return
  
  path_file = instance.search(0)["nome_do_arquivo"]
  instance.dequeue()
  print(f'Arquivo {path_file} removido com sucesso')



def file_metadata(instance, position):
    try:
      print(instance.search(position))
    except IndexError:
      sys.stderr.write('Posição inválida\n')
    

