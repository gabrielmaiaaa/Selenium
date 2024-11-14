from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Firefox()

navegador.get('http://localhost:5173/')

#Acessar cadastro
navegador.find_element(By.XPATH, '/html/body/div/div/nav/button').click()
time.sleep(1)
navegador.find_element(By.XPATH, '/html/body/div/div/div[1]/ul/li[7]/a').click()
time.sleep(1)

# Cadatrar Usuario
# Nome do cliente
navegador.find_element(By.XPATH, '//*[@id="name"]').send_keys('Maia')
time.sleep(0.5)
# Email do cliente
navegador.find_element(By.XPATH, '//*[@id="email"]').send_keys('maia67443@gmail.com')
time.sleep(0.5)
# Telefone do cliente
navegador.find_element(By.XPATH, '//*[@id="phone"]').send_keys('38999106743')
time.sleep(0.5)
# Senha do cliente
navegador.find_element(By.XPATH, '//*[@id="password"]').send_keys('teste12')
time.sleep(0.5)
# Confirmar Senha do cliente
navegador.find_element(By.XPATH, '//*[@id="confirmPassword"]').send_keys('teste12')
time.sleep(0.5)
# Endereço do cliente
navegador.find_element(By.XPATH, '//*[@id="address"]').send_keys('Rua Um, Bairro Dois, 230')
time.sleep(1)

# Cadastrar
navegador.find_element(By.XPATH, '/html/body/div/div/div/form/div/button').click()
time.sleep(1)
navegador.find_element(By.XPATH, '/html/body/div/div/div/form/div/button').click()

# Logar
# Email do cliente
navegador.find_element(By.XPATH, '//*[@id="email"]').send_keys('maia67443@gmail.com')
time.sleep(0.5)
# Senha do cliente
navegador.find_element(By.XPATH, '//*[@id="password"]').send_keys('teste12')
time.sleep(0.5)
# Logar
navegador.find_element(By.XPATH, '/html/body/div/div/div/form/div/button').click()
time.sleep(1)

# Verificar Dados
navegador.find_element(By.XPATH, '/html/body/div/div/nav/button').click()
time.sleep(1)
navegador.find_element(By.XPATH, '/html/body/div/div/div[1]/ul/li[5]/a').click()
time.sleep(1)

# Editar Dados
navegador.find_element(By.XPATH, '/html/body/div/div/div/form/div/button[1]').click()
time.sleep(1)
# Endereço do cliente
navegador.find_element(By.XPATH, '//*[@id="address"]').clear() 
time.sleep(0.5)
navegador.find_element(By.XPATH, '//*[@id="address"]').send_keys('Rua Josezin, Bairro Cardoso, 1400')
time.sleep(0.5)
navegador.find_element(By.XPATH, '/html/body/div/div/div/form/div/button[1]').click()
time.sleep(2)

# Deletar Usuario
navegador.find_element(By.XPATH, '/html/body/div/div/div/form/div/button[2]').click()
time.sleep(2)