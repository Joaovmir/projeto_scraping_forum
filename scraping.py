import pandas as pd
from auxiliares import abrir_pagina


def roda_scraping_off_topic():
    url = 'https://cursos.alura.com.br/forum/categoria-offtopic/sem-resposta/'
    soup = abrir_pagina(url)
    ultima_pagina = soup.find_all('a', {'class': 'paginationLink'})[-1].text
    url = url + ultima_pagina
    soup = abrir_pagina(url)
    qtd_topicos = (int(ultima_pagina)-1)*20 + len(soup.find_all('a', {'class': 'forumList-item-subject-info-title-link'}))
    return qtd_topicos


def roda_scraping_pagina_inicial():
    url = 'https://cursos.alura.com.br/forum/todos/1'
    soup = abrir_pagina(url)
    nomes = soup.find_all('a', {'class': 'dashboard-category-name-text'})
    quantidades = soup.find_all('span', {'class': 'category-stats-item-number dashboard-stats-noReply-number'})
    
    dados = {}
    for indice in range(len(nomes)):
        dados[f'{nomes[indice].text.strip()}'] = f'{quantidades[indice].text.strip()}'
    qtd_topicos_off_topic = roda_scraping_off_topic()
    dados['Off-Topic'] = qtd_topicos_off_topic
    df = pd.DataFrame(dados.items(), columns = ['Categoria', 'Tópicos sem resposta'])
    return df
