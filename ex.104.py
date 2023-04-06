import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.youtube.com/watch?v=kqezrec09TY&list=RDMMkqezrec09TY&start_radio=1')
except:
    print('Erro')
else:
    print('deu certo!')
    print(site.read())





