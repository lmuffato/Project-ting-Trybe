from importlib.resources import path
import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    data = txt_importer(path_file)
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None
   

def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
