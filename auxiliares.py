from dotenv import dotenv_values
from requests import get
from requests.models import HTTPError
from bs4 import BeautifulSoup

CONFIG = dotenv_values('.env')


def requisicao_api(url: str) -> 'json':
    '''
    Função que faz requisição a uma url, retornando um objeto do tipo JSON.
    '''

    try:
        response = get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'Um erro HTTP ocorreu: {http_err}')
    except Exception as err:
        print(f'Um erro ocorreu: {err}')
    else:
        return response.json()


def abrir_pagina(url: str) -> BeautifulSoup:
    '''
    Função que faz requisição a uma url, retornando o seu conteúdo através de um objeto do tipo BeautifulSoup.
    '''

    cookies = {'caelum.login.token': CONFIG['COOKIE']}
    try:
        response = get(url, cookies=cookies)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'Um erro HTTP ocorreu: {http_err}')
    except Exception as err:
        print(f'Um erro ocorreu: {err}')
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup


def tem_paginacao(soup):
    return True if soup.find('nav', {'class': 'busca-paginacao-links'}) else False