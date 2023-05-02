import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
import xlsxwriter

from gerador.models import Realty

workbook = xlsxwriter.Workbook('Imóveis com ERRO.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Imóvel com erro')

driver = webdriver.Chrome()

planilha = pd.read_excel('Imoveis.xlsx')
print(planilha)

driver.get('https://app.imoview.com.br/Login/LogOn?ReturnUrl=%2f')

driver.find_element(By.XPATH, ('//*[@id="campo_email_login"]')).send_keys('joao.rodrigues@imobiliariajazz.com')
driver.find_element(By.XPATH, ('//*[@id="botao_continuar_email_login"]')).click()
sleep(3)
driver.find_element(By.XPATH, ('//*[@id="container"]/div/div[1]/form/div[2]/div/div/div[4]/div/input')).send_keys('Rodrigues@82')
driver.find_element(By.XPATH, ('//*[@id="botao_acessar_sistema"]')).click()

start = input('Aperte qualquer coisa para iniciar\n')

cont = 2

for i in range(1000):
    codigo = planilha['Codigo'][i]
    tipo = planilha['Tipo'][i]
    valor = planilha['Valor'][i]
    bairro = planilha['Bairro'][i]
    cidade = planilha['Cidade'][i]
    area_t = planilha['AreaLote'][i]
    area_c = planilha['AreaInterna'][i]
    quartos = planilha['NumeroQuarto'][i]
    suites = planilha['NumeroSuite'][i]
    banheiros = planilha['NumeroBanheiro'][i]
    vagas = planilha['NumeroVaga'][i]
    
    try:
        quartos = int(quartos)
        suites = int(suites)
        banheiros = int(banheiros)
        vagas = int(vagas)
        
    except Exception as error:
        print(error)

    descricao = Realty(tipo, valor, quartos, suites, banheiros, vagas, area_c, area_t, bairro, cidade)

    driver.get(f'https://app.imoview.com.br/Imovel/Alterar/{codigo}')

    caixa_texto = wdw(driver, 100).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="painelDadosPrincipais"]/div/div[4]/div[9]/textarea')))
    caixa_texto.clear()
    caixa_texto.send_keys(descricao.run())
    print(descricao.run())

    sleep(1)

    driver.find_element(By.XPATH, '//*[@id="page-content"]/form/div[1]/div/ul[2]/li/div/button').click()

    sleep(4)

    current_url = str(driver.current_url)
    print(f'URL ATUAL: {current_url}')

    expected_url = f'https://app.imoview.com.br/Imovel/Detalhes/{codigo}'
    expected_url = expected_url.strip('\n')
    print(f'URL Esperado: {expected_url}')

    if current_url == expected_url:
        print('Alterado com sucesso\n\n')
    else:
        print('Erro na porcentagem\n\n')
        worksheet.write(f'A{cont}', codigo)
        cont = cont + 1

workbook.close()
