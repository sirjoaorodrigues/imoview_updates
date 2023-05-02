from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

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
    WebDriverWait(driver, 100).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="mainnav-menu"]/li[5]')))
    driver.find_element(By.XPATH, '//*[@id="mainnav-menu"]/li[5]').click()
    WebDriverWait(driver, 100).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="form1"]/div[1]/div[1]/div/input')))

    f = open("codes/adicionar.txt", "r")

    for i in f:
        driver.find_element(By.XPATH, '//*[@id="form1"]/div[1]/div[1]/div/input').send_keys(f'{i}\n')


if __name__ == '__main__':
    login()
    start = input('Digite "1" para começar\n')
    if start == '1':
        run_aplication()
        sleep(100000)
    else:
        print('Fim de Execução')
