import speedtest
from time import sleep
from os import system
from os.path import exists
from datetime import datetime

s = speedtest.Speedtest()
s.get_best_server()
s.download()
s.upload()

ping = s.results.dict()['ping']
download = s.results.dict()['download'] / 1000000
upload = s.results.dict()['upload'] / 1000000