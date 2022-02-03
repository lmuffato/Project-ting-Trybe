from ting_file_management.queue import Queue
import regex

def count_words(word, word_to_count):
    r = regex.compile(f"({word.lower()})")
    out = r.findall(word_to_count.lower())
    return len(out)

def exists_word(word: str, instance: Queue):
    output = []
    for index in range(len(instance)):
      file = instance.search(index)
      palavra = word
      arquivo = file["nome_do_arquivo"]
      lines = file["linhas_do_arquivo"]

      ocorrencias = [
        {
          "linha": line_num + 1,
        }
        for line, line_num in zip(lines, range(len(lines)))
        if count_words(word, line) != 0
      ]
      if len(ocorrencias) != 0:
        output.append({
          "palavra": palavra,
          "arquivo": arquivo,
          "ocorrencias": ocorrencias
        })
      return output

    


def search_by_word(word, instance):
    output = []
    for index in range(len(instance)):
      file = instance.search(index)
      palavra = word
      arquivo = file["nome_do_arquivo"]
      lines = file["linhas_do_arquivo"]

      ocorrencias = [
        {
          "linha": line_num + 1,
          "conteudo": line
        }
        for line, line_num in zip(lines, range(len(lines)))
        if count_words(word, line) != 0
      ]
      if len(ocorrencias) != 0:
        output.append({
          "palavra": palavra,
          "arquivo": arquivo,
          "ocorrencias": ocorrencias
        })
      return output
