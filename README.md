# CASE: Projeto seletivo

Esse projeto tem como objetivo ter a função de um software que extrai informações da base
de dados do Spotify, a partir dessa análise e extração, é feita a criação de dois rankings, 
um com artistas do gênero 'pop' ordenados por número de seguidores, incluindo também sua 
popularidade e outro que mostra os gêneros mais comuns.

## Etapas do projeto de acordo com o Script na documentação:

### Etapa 1: Escolha da linguagem.

A linguaguem escolhida para o desenvolvimento da solução foi Python, o editor de 
código escolhido foi o VS Code [Visual Studio Code](https://code.visualstudio.com/).

### Etapa 2: Criação do aplicativo.

Nessa etapa houve a criação do aplicativo no [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications)
para ambientação, obtive as variáveis 'CLIENT_ID' e 'CLIENT_SECRET'.

### Etapa 3: Autenticação do App.

Após a leitura da documentação sobre a autorização das credenciais, obtive o token 
de acesso pelo [POSTMAN](https://www.postman.com/).

### Etapa 4: Requisições na API do Spotify.

Nessa etapa, após a leitura da documentação, foi possivel acessar os dados na API
e consultar todos os 15 artistas pré-selecionados presentes no enunciado, foi extraido
no script principal `app.py`. 

### Etapa 5: Construção da página web responsiva.

A página web foi desenvolvida usando HTML e JavaScript, HTML para estrutura da página
e o JavaScript para manipulação dos dados da API do Spotify, o CSS foi responsável
pelo design final. Sua funcionalidade foi exibir os rankings de artista pop e gêneros 
mais comuns. A página foi feita também para se adaptar a qualquer tamanho de tela.

### Etapa 6: Subir o projeto em um repositório público do github.

## Arquivos

`app.py`: Script principal para extrair dados da API do Spotify.
`spotify_data.py`: Funções auxiliares para manipulação de dados.
`index.html`: Página web responsiva para exibição dos rankings.


Adicionei um novo repositório em meu perfil do Github e iniciei os comandos
no terminal do próprio editor de código. 

Esses foram os passos:
```bash
pip install flask
```
```bash
pip install requests
```
```bash
pip install dotenv
```
```bash
git init
```
```bash
git add.
```
```bash
git commit -m "Case commit"
```
```bash
git remote add origin <https://github.com/vitellys/rakingdosartistasspotify>
```
```bash
git push -u origin main.
```

## Etapa 7: Requisição do tipo POST. 

Apos utilizar a biblioteca requests para enviar o POST, o código foi executado
no terminal com o seguinte comando: python requisicao_post.py.

Essa foi a resposta do terminal: 

200
{"msg":"Thank you for submitting your response."}

### Etapa Final: 

Como executar o projeto:

Primeiro, abra o terminal e digite os seguintes comandos:

- Clone o repositório:
  ```bash
  git clone https://github.com/https://github.com/vitellys/rakingdosartistasspotify.git
  ```
- Instale as dependências:
    ```bash
    pip install requests
    ```
     ```bash
    pip install flask
    ```
    ```bash
    pip install dotenv
    ```
- Execute o script:
    ```bash
    python app.py
    ```
    
Enquanto pressiona 'Ctrl' clique com o botão esquerdo do mouse no link que o terminal
resultará, aguarde a página carregar por completa e aparecerá os dados completos. 

Obs: As alterações de comentários nos códigos foram aperfeiçoadas, adicionadas e simplificadas afim de deixar o código com fácil entendimento.  
