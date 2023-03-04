from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import mysql.connector


class Financas:
    def __init__(self):
        self.browser = None
        
        

    def iniciar(self):
        self.conect()
        self.config_browser()
        self.dados_yahoo()
        self.envio_bd()
        
    def conect (self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user='root',
            password='1234',
            database='teste'
            
        )
        
        self.cursor = self.conn.cursor()
        self.query = "SELECT * FROM app_ticket"
        self.cursor.execute(self.query)
        self.data = self.cursor.fetchall()
        

    def config_browser(self):
        options = Options()
        options.add_argument('--headless')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.browser = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options)
        
        
    def dados_yahoo(self):
        try:
            for row in self.data:
                self.ticket = row[1]
                
                
                print(self.ticket)
                
                url = f'https://finance.yahoo.com/quote/{self.ticket}.SA'
                print(url)
                self.browser.get(url)
                
                
                self.company = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="Mt(15px) D(f) Pos(r)"]//div[1]//div[@class="D(ib) "]//h1'))).text
                
                self.preco = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="D(ib) Mend(20px)"]//fin-streamer[1]'))).text
                
                self.aumento = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="D(ib) Mend(20px)"]//fin-streamer[2]'))).text
                
                self.porcentagem = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="D(ib) Mend(20px)"]//fin-streamer[3]'))).text
                
                print(self.ticket)
                print('Company:', self.company[:-12].strip())
                print('preço atual:', self.preco)
                print('aumento:', self.aumento)
                print('Porcentagem do aumento:', self.porcentagem)
                sleep(2)
                self.renda_infomoney()
                
        except TimeoutException and NoSuchElementException:
            print("Error: Timed out waiting for elements to load")

    def renda_infomoney(self):
        self.link = f'https://www.infomoney.com.br/cotacoes/b3/fii/fundos-imobiliarios-{self.ticket}/'
        print(self.link)
        self.browser.get(self.link)
        try:
            self.rendimento = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/main/section/div/div/div[2]/div/div[1]/div[2]'))).text
            
            self.yield_m = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/main/section/div/div/div[2]/div/div[2]//span'))).text
            
            self.yield_ano = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/main/section/div/div/div[2]/div/div[4]//span'))).text
            
            
            
            print('Último rend:', self.rendimento.split()[1])
            print('Yield 1M:', self.yield_m[:-1])
            print('Yield 12M:', self.yield_ano[:-1])
            print(datetime.now())

        except NoSuchElementException as e:
            print(f"Error {e}")
            return
        
        
        
        self.yield_m = self.yield_m.replace(",", ".")[:-1]
        self.yield_ano = self.yield_ano.replace(",", ".")[:-1]
        self.rendimento = self.rendimento.split()[1].replace(",", ".")
        self.company = self.company[:-12].strip()
        
        
        
        
        
        self.px_rendimento = (float(self.yield_m) / 100) * float(self.preco)
        print(f'PX_rend: {self.px_rendimento:.2f}')
        
    def envio_bd(self):
        self.env = "SELECT * FROM app_ticket WHERE ticket"
        self.cursor.execute(self.env)
        
        self.cursor.fetchone()
        
        cmd = f'''UPDATE app_ticket SET company = "{self.company}",price = "{self.preco}",preco_mercado = "{self.aumento}", mercado_percente = "{self.porcentagem[2:-2]}",
                       rendimento = "{self.rendimento}", px_rendimento = "{self.px_rendimento:.2f}",
                       yld_mes = "{self.yield_m}",yld_ano = "{self.yield_ano}", datatime = "{datetime.now()}" WHERE ticket = "{self.ticket}"  '''
        self.cursor.execute(cmd)
        self.conn.commit()
        
        self.cursor.close()
        self.conn.close()    
