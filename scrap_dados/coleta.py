from dados_yahoo import *
import time

while True:
    init = Financas()
    init.iniciar()
    for x in range(15,0,-1):
        sec = x % 60

        print(f'TIMER   00:{sec:02}', end='\r')
        time.sleep(1)
