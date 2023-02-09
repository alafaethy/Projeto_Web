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


class Financas:
    def __init__(self):
        # self.codigo = input('INFORME O CODIGO: ')
        self.codigo = 'VGHF11'
        self.url = f'https://finance.yahoo.com/quote/{self.codigo}.SA'
        self.browser = None

    def iniciar(self):
        self.config_browser()
        self.dados_yahoo()
        self.renda_infomoney()
        self.dados_site()

    def config_browser(self):
        options = Options()
        options.add_argument('--headless')

        self.browser = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options)
        self.browser.get(self.url)

    def dados_yahoo(self):
        try:
            preco = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="D(ib) Mend(20px)"]//fin-streamer[1]')))
            aumento = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="D(ib) Mend(20px)"]//fin-streamer[2]')))
            porcentagem = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="D(ib) Mend(20px)"]//fin-streamer[3]')))

            print(self.codigo)
            print('preço atual:', preco.text)
            print('aumento:', aumento.text)
            print('Porcentagem do aumento:', porcentagem.text)
            sleep(2)
        except TimeoutException:
            print("Error: Timed out waiting for elements to load")

    def renda_infomoney(self):
        self.link = f'https://www.infomoney.com.br/cotacoes/b3/fii/fundos-imobiliarios-{self.codigo}/'
        self.browser.get(self.link)

    def dados_site(self):
        try:
            rendimento = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/main/section/div/div/div[2]/div/div[1]/div[2]')))
            yield_m = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/main/section/div/div/div[2]/div/div[2]//span')))
            yield_ano = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/main/section/div/div/div[2]/div/div[4]//span')))

            print('Último rend:', rendimento.text)
            print('Yield 1M:', yield_m.text)
            print('Yield 12M:', yield_ano.text)
            print(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

        except NoSuchElementException as e:
            print(f"Error {e}")
            return
        finally:
            self.browser.quit()