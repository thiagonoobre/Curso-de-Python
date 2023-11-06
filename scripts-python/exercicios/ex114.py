import requests


def verificação(site):
    try:
        requests.get(site)
    except requests.ConnectionError:
        print('Não conseguimos acessa o site')
    else:
        print('Conseguimos acessa o site')


url = 'https://twitter.com/home'
verificação(url)
