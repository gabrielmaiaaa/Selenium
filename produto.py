from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Firefox()

navegador.get('http://localhost:5173/')

# Clicando até registrar um produto
navegador.find_element(By.XPATH, '/html/body/div/div/nav/button').click()
time.sleep(1)
navegador.find_element(By.XPATH, '/html/body/div/div/div[1]/ul/li[1]/a').click()
time.sleep(1)
navegador.find_element(By.XPATH, '/html/body/div/div/div/div/button[2]/a').click()
time.sleep(1)

# Cadastrar produto
# ID do produto
navegador.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[1]/input').send_keys('58468')
time.sleep(0.5)
# Nome do produto
navegador.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[2]/input').send_keys('Pão de queijo')
time.sleep(0.5)
# Categoria do produto
navegador.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[3]/select/option[3]').click()
time.sleep(0.5)
# Preço do produto
navegador.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[4]/input').send_keys('3.50')
time.sleep(0.5)
# Descrição do produto
navegador.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[5]/textarea').send_keys('Uma caixa de pão de queijo de 500g')
time.sleep(1)
# Enviar
navegador.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[6]/button[1]').click()
time.sleep(2)

# Excluir Produto
navegador.find_element(By.XPATH, '/html/body/div/div/div/table/tbody/tr[1]/td[7]/button[2]').click()
time.sleep(2)

# Editar Produto
navegador.find_element(By.XPATH, '/html/body/div/div/div/table/tbody/tr[1]/td[7]/button[1]').click()
time.sleep(1)
# Limpando dados
navegador.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[6]/button[2]').click()
time.sleep(1)
# Nome do produto
navegador.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[2]/input').send_keys('Salgadinhos')
time.sleep(0.5)
# Categoria do produto
navegador.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[3]/select/option[3]').click()
time.sleep(0.5)
# Preço do produto
navegador.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[4]/input').send_keys('13.50')
time.sleep(0.5)
# Descrição do produto
navegador.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[5]/textarea').send_keys('Um montão de salgadinho')
time.sleep(1)
# Enviar
navegador.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[6]/button[1]').click()
time.sleep(2)
