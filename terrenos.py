from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
import xlsxwriter

driver = webdriver.Chrome()

workbook = xlsxwriter.Workbook('Imóveis com ERRO.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Imóvel com erro')


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
    f = open("terrenos.txt", "r")

    for i in f:

        driver.get(f'https://app.imoview.com.br/Imovel/Alterar/{i}')
        print(i.strip('\n'))

        wdw(driver, 100).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="painelAreas"]/div/div[1]/div[1]/input')))

        terrain = driver.find_element(By.XPATH, '//*[@id="painelAreas"]/div/div[1]/div[1]/input').get_attribute('value')

        external = driver.find_element(By.XPATH, '//*[@id="painelAreas"]/div/div[1]/div[2]/input').get_attribute('value')

        driver.find_element(By.XPATH, '//*[@id="painelAreas"]/div/div[1]/div[3]/input').clear()

        try:

            driver.find_element(By.XPATH, '//*[@id="painelAreas"]/div/div[1]/div[3]/input').send_keys('{0:.2f}'.format(external_area(external, calc(terrain))))

        except Exception as e:
            print(e, 'Ocorreu um erro!')

        sleep(2)

        driver.find_element(By.XPATH, '//*[@id="page-content"]/form/div[1]/div/ul[2]/li/div/button').click()

        sleep(4)

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

    workbook.close()


def external_area(external, value):
    try:
        external = external.replace(',','.')
        external = float(external)
    except ValueError:
        return 200
    if external > value:
        return external + 1
    else:
        return value


def calc(n):
    try:
        n1 = n.replace(',','.')
        number = float(n1)
        res = 25 // (number/100)
        ans = number + res
        return ans
    except ValueError:
        return 200


if __name__ == '__main__':
    login()
    start = input('Digite "1" para começar\n')
    if start == '1':
        run_aplication()
    else:
        print('Fim de Execução')
