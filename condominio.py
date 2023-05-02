from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
import xlsxwriter

workbook = xlsxwriter.Workbook('Imóveis com ERRO Condominio.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Imóvel com erro')

driver = webdriver.Chrome()

def login():
    driver.get('https://app.imoview.com.br/Login/LogOn?ReturnUrl=%2f')

    driver.find_element(By.XPATH, ('//*[@id="campo_email_login"]')).send_keys('joao.rodrigues@imobiliariajazz.com')
    driver.find_element(By.XPATH, ('//*[@id="botao_continuar_email_login"]')).click()
    sleep(3)
    driver.find_element(By.XPATH, ('//*[@id="container"]/div/div[1]/form/div[2]/div/div/div[4]/div/input')).send_keys(
        'Rodrigues@82')
    driver.find_element(By.XPATH, ('//*[@id="botao_acessar_sistema"]')).click()


def run_aplication():
    cont = 2
    f = open("codes/condominio.txt", "r")

    for i in f:
        driver.get(f'https://app.imoview.com.br/Imovel/Alterar/{i}')

        wdw(driver, 100).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="CondominioImovel"]')))

        driver.find_element(By.XPATH,'//*[@id="CondominioImovel"]').send_keys('199,90')

        driver.find_element(By.XPATH, '//*[@id="page-content"]/form/div[1]/div/ul[2]/li/div/button').click()

        sleep(2)

        current_url = str(driver.current_url)
        print(f'URL ATUAL: {current_url}')

        expected_url = f'https://app.imoview.com.br/Imovel/Detalhes/{i}'
        expected_url = expected_url.strip('\n')
        print(f'URL Esperado: {expected_url}')

        if current_url == expected_url:
            print('Alterado com sucesso\n\n')
        else:
            print('Erro na porcentagem\n\n')
            worksheet.write(f'A{cont}', i)
            cont = cont + 1


if __name__ == '__main__':
    login()
    start = input('Digite "1" para começar\n')
    if start == '1':
        run_aplication()
        workbook.close()
        sleep(10)
    else:
        print('Fim de Execução')
