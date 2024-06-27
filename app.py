# O PROJETO DEVE CONTER UMA UNICA SEQUENCIA!
import pandas as pd
import xml.etree.ElementTree as ET
import re

# Carregar o arquivo XML
tree = ET.parse('1SEQ/EXTRACTION_TEST.xml')
root = tree.getroot()
lista_tracks = []

# Função recursiva para buscar todas as tags 'clipitem'

def buscar_clipitems_stereo(element):
    clipitems = []
    if element.tag == 'clipitem' and element.get('premiereChannelType') == 'stereo':
        clipitems.append(element)
    for child in element:
        clipitems.extend(buscar_clipitems_stereo(child))
    return clipitems

#Função para verificar se existe duplicidade da track na lista
def comparar_track(lista, track):
    for t in lista:
        if t['NOME'] == track['NOME'] and t['DURACAO'] == track['DURACAO']:
            return True
    return False


# Função principal para processar o XML e extrair informações das 'clipitem'
def catalogar_tracks():
    clipitems = buscar_clipitems_stereo(root)
    for clipitem in clipitems:
        nome = clipitem.find('name').text.upper()
        if '_' and '#' in nome:
            splitters = r'[_#]'
            nome = re.split(splitters, nome)
            in_point = int(clipitem.find('in').text)
            out_point = int(clipitem.find('out').text)
            duration = round((out_point - in_point)/29.97)
            armazena_track = {
                'NOME': nome[1], 'ARTISTA': nome[3], 'DURACAO': duration}
            if armazena_track and not comparar_track(lista_tracks, armazena_track):
                lista_tracks.append(armazena_track)
        else:
            pass

# Função para transformar a lista em string
def fazer_ecad():
    for track in lista_tracks:
        print(
            f"NOME: {track['NOME'].ljust(35)} | ARTISTA: {track['ARTISTA'].ljust(35)} | DURAÇÃO: {track['DURACAO']}")

# Função para converter para excel
def converter_para_excel():
    df = pd.DataFrame(lista_tracks)
    df.to_excel('exports/ECAD_export.xlsx', index=False)
    print('Dados exportados com sucesso!')


# Chamar a função para processar o XML
catalogar_tracks()
fazer_ecad()
converter_para_excel()




