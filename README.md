# ScrapeUOL

ScrapeUOL é um projeto de web scraping que coleta os títulos das notícias do site [UOL Notícias](https://noticias.uol.com.br) e permite salvá-los em um arquivo de texto.

## Requisitos

Antes de executar o projeto, certifique-se de ter o Python instalado em sua máquina e as dependências necessárias. Para instalá-las, utilize o seguinte comando:

```
pip install -r requirements.txt
```

## Como Executar

1. Clone este repositório ou baixe o arquivo `main.py`:
   ```
   git clone https://github.com/caioreis29974/ScrapeUOL.git
   cd ScrapeUOL
   ```
2. Navegue até o diretório do projeto, caso ainda não tenha feito isso:
   ```
   cd ScrapeUOL
   ```
3. Execute o script:
   ```
   python main.py
   ```
4. O script exibirá os títulos das notícias no terminal.
5. Quando solicitado, digite `Y` para salvar os títulos em um arquivo de texto ou `N` para encerrar o programa sem salvar.

## Estrutura do Projeto

```
ScrapeUOL/
├── main.py             # Script principal para scraping e salvamento dos dados.
├── requirements.txt    # Lista de dependências necessárias.
├── README.md           # Documentação do projeto.
├── LICENSE             # Arquivo de licença.
```

## Tecnologias Utilizadas

- Python 3+
- Requests (para obter as páginas da web)
- BeautifulSoup (para extrair os dados desejados do HTML)

## Contribuição

Contribuições são bem-vindas! Se quiser sugerir melhorias ou corrigir problemas, abra uma [issue](https://github.com/caioreis29974/ScrapeUOL/issues) ou envie um [pull request](https://github.com/caioreis29974/ScrapeUOL/pulls).

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
