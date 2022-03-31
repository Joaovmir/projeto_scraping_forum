# Scraping e classificação de tópicos no fórum da Alura

# Sumário :bookmark_tabs:

1. [Resumo](#resumo)
2. [Tecnologias utilizadas](#tecnologias-utilizadas)
3. [Estrutura do projeto](#estrutura-do-projeto)
4. [Resumo de cada notebook](#resumo-de-cada-notebook)
5. [Desenvolvimento](#desenvolvimento)
6. [Conclusão](#conclusão)
7. [Contato](#contato)

<a name="resumo"></a>
# Resumo :page_with_curl:

Os fóruns são instrumentos de melhora da qualidade de aprendizado dos alunos e fornecem condições de melhoria dos conteúdos que estão sendo transmitidos para os estudantes. Diante da importância dos fóruns de discussão e da presença dos tutores para o aprendizado, é essencial para a comunidade escolar que o máximo de dúvidas sejam sanadas. A Alura, uma escola de tecnologia, possui um fórum de discussão com visualização pública na internet e uma equipe especializada de tutores destinada a sanar as dúvidas dos alunos. O trabalho teve como objetivo a construção de estratégias para redução de tópicos sem resposta no fórum que estavam acumulados na área de Data Science, além de categorizar tópicos que não possuíam categoria definida em alguma das áreas de estudo oferecidas na plataforma da Alura. Os dados foram obtidos através de webscraping, utilizando a biblioteca BeautifulSoup para manipular códigos HTML. Alguns modelos de classificação foram utilizados e comparados para a categorização de tópicos sem categoria, fazendo uso de técnicas de processamento de linguagem natural (NLP) para transformar os textos extraídos do site em dados estruturados que podem ser compreendidos pelos modelos. As estratégias adotadas se mostraram eficientes, reduzindo a quantidade de tópicos sem resposta na área de Data Science e o modelo de classificação obteve uma acurácia de teste acima do modelo base, alcançando uma classificação dos tópicos de forma satisfatória.

<a name="tecnologias-utilizadas"></a>
# Tecnologias utilizadas :computer:

- dotenv 16.0.0
- requests 2.24.0
- bs4 4.9.3
- pandas 1.2.3
- numpy 1.19.2
- nltk 3.5
- sklearn 0.23.2

<a name="estruturas-do-projeto"></a>
# Estrutura do projeto :card_index_dividers:

O projeto possui uma pasta contendo os notebooks utilizados para realizar o webscraping e modelagem bem como arquivo requirements com as bibliotecas necessárias para execução do código. A ordem de leitura dos notebooks pode ser encontrada a seguir:

1. [Página inicial](https://github.com/Joaovmir/projeto_scraping_forum/blob/master/notebooks/pagina_inicial.ipynb)
2. [Subcategorias](https://github.com/Joaovmir/projeto_scraping_forum/blob/master/notebooks/subcategorias.ipynb)
3. [Cursos](https://github.com/Joaovmir/projeto_scraping_forum/blob/master/notebooks/cursos.ipynb)
4. [Textos fórum](https://github.com/Joaovmir/projeto_scraping_forum/blob/master/notebooks/textos_forum.ipynb)
5. [Base treino e teste](https://github.com/Joaovmir/projeto_scraping_forum/blob/master/notebooks/base_treino_teste.ipynb)
6. [Classificação de tópicos](https://github.com/Joaovmir/projeto_scraping_forum/blob/master/notebooks/classificacao_topicos.ipynb)

<a name="resumo-de-cada-notebook"></a>
# Resumo de cada notebook :books:

## 1 - Página inicial

Foi realizado o scraping na [página inicial do fórum da Alura](https://cursos.alura.com.br/forum/todos) e extraído a quantidade de tópicos sem resposta em cada uma das áreas de estudo da plataforma.

## 2 - Subcategorias

Foi realizado o scraping nas seções do fórum da Alura de cada subcategoria das áreas de estudo, extraindo a quantidade de tópicos sem resposta por cada subcategoria.

## 3 - Cursos

Foi realizado o scraping nas seções do fórum da Alura de cada curso da plataforma, extraindo a quantidade de tópicos sem resposta para cada curso.

## 4 - Textos fórum

Foi realizado scraping nas seções do fórum de cada área de estudo, extraindo os links e títulos de uma amostra de tópicos. Em seguida, os links foram acessados e através de scraping, o texto da pergunta de cada um dos tópicos foi extraída e salvos em tabelas.

## 5 - Base treino e teste

Os dados textuais foram divididos em dados de treino e teste para a modelagem de dados no último notebook

## 6 - Classificação de tópicos

As bases de dados de treino e teste foram tratadas com ferramentas de NLP e diversos modelos foram treinados e comparados. Um modelo foi selecionado, e por fim, foram classficados os tópicos sem categoria.

<a name="desenvolvimento"></a>
# Desenvolvimento :hammer_and_wrench:

O fórum da Alura é dividido em 7 grandes áreas de estudo e uma seção denominada “Off-topic”, que apresenta tópicos com assuntos diversos. Dentro das áreas de estudo, existem diversas subcategorias e cursos. O intuito era descobrir a quantidade de tópicos existentes em cada subcategoria e cada um dos cursos, para que a equipe responsável por responder ao fórum tenha um melhor direcionamento de resposta, eliminando possíveis gargalos e acúmulos.

Os dados foram obtidos nas páginas web do fórum de discussão através de “webscraping” com a linguagem Python. Através do HTML das páginas, foi possível fazer a contagem da quantidade de tópicos e armazenar em arquivos com extensão csv, que são arquivos com texto separados por vírgula, armazenados em um formato de banco de dados.

Além disso, foi possível extrair os textos dos tópicos através do “HTML” das páginas. Esses textos foram tratados através de processamento de linguagem natural, e diversos modelos de classificação foram construídos a partir dos tópicos que já possuem categorização de áreas de estudo. Através do treinamento do modelo, foi possível classificar os tópicos existentes na seção “Off-topic”, para tópicos que apresentam conteúdo relacionado a alguma área de estudo já existente no fórum.

O problema era uma classificação multinomial com 7 classes, sendo elas: Mobile, Programação, Front-end, DeVops, UX & Design, Data Science e Inovação & Gestão. Os modelos construídos para realizar a classificação, bem como o resultado obtido por cada um deles após os tratamentos dos dados foi o seguinte:

|       |       **Modelo**       | **Acurácia de treino** | **Acurácia de teste** |
|:-----:|:----------------------:|:----------------------:|:---------------------:|
| **0** |     DummyClassifier    |        0.143237        |        0.140880       |
| **1** |   LogisticRegression   |        0.552587        |        0.513194       |
| **2** |      MultinomialNB     |        0.712018        |        0.678731       |
| **3** | DecisionTreeClassifier |        0.994183        |        0.548666       |
| **4** |           SVM          |        0.811771        |        0.716799       |

A acurácia foi a métrica utilizada para comparar os modelos uma vez que o objetivo era a melhor taxa de acerto possível do modelo em relação a todas as categorias. O modelo SVM foi o escolhido e foi realizado um tuning de parâmetros, porém não surtiu o resultado desejado, uma vez que sofreu overfitting.

Parâmetros do modelo após o tuning: `{'kernel': 'rbf', 'C': 10, 'gamma': 'scale',}`

Resultado do modelo após o tuning: 

|       | **Modelo** | **Acurácia de treino** | **Acurácia de teste** |
|:-----:|:----------:|:----------------------:|:---------------------:|
| **0** |     SVM    |        0.994075        |        0.728479       |

Parâmetros do modelo escolhido: `{'kernel': 'linear', 'C': 1, 'gamma': 'scale'}`

Resultado do modelo escolhido:

|       | **Modelo** | **Acurácia de treino** | **Acurácia de teste** |
|:-----:|:----------:|:----------------------:|:---------------------:|
| **0** |     SVM    |        0.811771        |        0.716799       |

<a name="conclusão"></a>
# Conclusão :round_pushpin:

A coleta de dados quantitativos de tópicos se mostrou satisfatória e foi muito útil para aplicação de projetos para redução da quantidade de tópicos sem resposta na seção de Data Science do fórum da Alura.

Os tópicos categorizados podem facilitar o trabalho da equipe que responde ao fórum, ao passo que pessoas específicas podem ser designadas a tópicos da área de estudo que tiver maior afinidade.

A construção do modelo de classificação poderia ser utilizado futuramente em uma classificação automática de tópicos ou sugestão de classificação para autores dos tópicos no momento da criação das perguntas.

<a name="contato"></a>
# Contato :envelope_with_arrow:

Caso queira entrar em contato para sugestões, dúvidas ou algo relacionado, sinta-se à vontade para enviar um e-mail ou mensagem através do linkedin.

[<img src="https://img.shields.io/badge/joaovmiranda-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/joaovmiranda/)  [<img src="https://img.shields.io/badge/Gmail-EA4335?style=flat-square&logo=Gmail&logoColor=white" />](mailto:joao.miranda27@gmail.com)