# Site está acessível?

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com.br/?gws_rd=ssl')
except:
    urllib.error.URLError
    print(f'O site Google não está acessível no momento.')
else:
    print(f'O site Google foi acessado com sucesso!')
    print(site.read())