### README.md

# 🎵 Catalogador de Trilhas Sonoras para Projetos do Premiere Pro

Bem-vindo ao **Catalogador de Trilhas Sonoras**! Este script em Python automatiza o processo de catalogação de trilhas sonoras usadas em projetos do Premiere Pro salvos como arquivos .xml. Ele identifica e cataloga as trilhas, fornecendo detalhes como o nome da trilha, o artista e a duração. O resultado é exportado em um arquivo .xlsx. Esta automação ajuda a simplificar o processo manual conhecido como ECAD para catalogação de informações de direitos autorais.

## 🚀 Funcionalidades

- **Identificação Automática de Trilhas**: Extrai informações das trilhas a partir de arquivos .xml.
- **Catalogação**: Lista o nome da trilha, o artista e a duração.
- **Exportação para Excel**: Gera um arquivo .xlsx com as informações catalogadas.

## 🛠️ Como Usar

1. **Clone o repositório**:
    ```sh
    git clone https://github.com/eduardocorgos/catalogo-de-trilhas
    ```

2. **Instale as dependências**:
    ```sh
    pip install -r requirements.txt
    ```
3. **Indique o caminho do arquivo .xml**: No script `catalogador.py`, substitua o caminho do arquivo .xml nas linhas 6 e 7:
    ```python
    # Carregar o arquivo XML
    tree = ET.parse('caminho/para/seu/arquivo.xml')
    ```
4. **Execute o script**:
    ```sh
    python app.py 
    ```

   Certifique-se de que as trilhas sigam a convenção de nomes: `genero_nomeDaMusica_nomeDoArtista#codigo`.

## ⚠️ Limitações Conhecidas

- **Convenção de Nomes**: As trilhas precisam seguir a convenção de nomes especificada. Melhorias futuras podem incluir identificação por IA para aumentar a flexibilidade.
- **Taxa de Quadros**: A linha do tempo deve estar configurada para 29,97 quadros por segundo. Uma melhoria futura pode incluir uma variável para armazenar essa informação.

## 🛡️ Trabalho em Andamento

Este projeto está em andamento (WIP). Contribuições e sugestões são super bem-vindas!

---

Sinta-se à vontade para entrar em contato com qualquer dúvida ou sugestão. Feliz codificação!
