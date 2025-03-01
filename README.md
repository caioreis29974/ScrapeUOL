# ScrapeUOL

Este projeto faz a coleta de notícias do site [UOL Notícias](https://noticias.uol.com.br) e permite salvar os títulos das notícias em um arquivo de texto.

## Requisitos

Antes de executar o projeto, certifique-se de ter instalado as dependências necessárias. Você pode instalá-las usando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Como Executar

1. Clone este repositório ou baixe o arquivo *main.py*:
```bash
git clone https://github.com/caioreis29974/ScrapeUOL.git
```
2. Navegue até o diretório do projeto.
```bash
cd ScrapeUOL
```
3. Execute o script Python:
```bash
python main.py
```
4. O script exibirá os títulos das notícias no terminal.
5. Você será perguntado se deseja salvar as notícias em um arquivo de texto. Digite Y para salvar ou N para encerrar o programa sem salvar.

## Estrutura do Projeto

ScrapeUOL/
│-- main.py              # Script principal para scraping e salvamento dos dados.
│-- requirements.txt     # Lista de dependências necessárias.
│-- README.md            # Documentação do projeto.
│-- LICENSE              # Arquivo de licença.

## Tecnologias Utilizadas

- Python 3+
- Requests (para obter a página da web)
- BeautifulSoup (para extrair os dados desejados do HTML)

## Contribuição

Se você quiser contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
