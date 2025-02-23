from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Escolher conta
conta = input("Qual conta você vai publicar? ")

# Abrir Chrome
browser = webdriver.Chrome()

# Entrar no site
browser.get("https://www.linkedin.com/login")

# Aumentar a janela
browser.maximize_window()

# Fazer login 
input_email = browser.find_element("id","username")
input_email.send_keys("seuemail@gmail.com")

input_senha = browser.find_element("id","password")
input_senha.send_keys("senha")

btn_login = browser.find_element(By.XPATH, "//button[@type='submit']")
btn_login.click()

time.sleep(10)

# Clicar em todas as contas
lista_btnhome = browser.find_elements(By.XPATH, "//button[@type='button']")

for btn in lista_btnhome:
    if "Veja tudo" in btn.text:
        btn.click()
        break

# Selecionar a conta
lista_contas = browser.find_elements(By.XPATH, "//span[@class='t-14 t-black t-bold block truncate mb1']")

for contas in lista_contas:
    if conta in contas.text:
        contas.click()
        break

time.sleep(2)

# Menu criar
lista_btncc = browser.find_elements(By.XPATH, "//span[@class='artdeco-button__text']")

for btncc in lista_btncc:
    if "Criar" in btncc.text:
        btncc.click()
        break

time.sleep(1)

# Criar publicação
lista_menu = browser.find_elements(By.XPATH, "//span[@class='org-menu-item__title org-menu-item__stateful-content text-body-medium-bold']")

for menu in lista_menu:
    if "Começar publicação" in menu.text:
        menu.click()
        break

time.sleep(2)

# Colar legenda
escrever = browser.find_element(By.XPATH, "//div[@class='ql-editor ql-blank']")
escrever.click()
time.sleep(2)
colar = ActionChains(browser)
colar.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep (2)

# Selecionar foto
foto = browser.find_element(By.XPATH, "//span[@class='share-promoted-detour-button__icon-container']")
foto.click()

time.sleep(10)

# Avançar confirmação
lista_btnfoto = browser.find_elements(By.XPATH, "//button[@type='button']")

for avançar in lista_btnfoto:
    if "Avançar" in avançar.text:
        avançar.click()
        break

time.sleep(2)

# Publicação do material
lista_final = browser.find_elements(By.XPATH, "//button[@class='share-actions__primary-action artdeco-button artdeco-button--2 artdeco-button--primary ember-view']")

for publicacao in lista_final:
    if "Publicar" in publicacao.text:
        publicacao.click()
        break

# Aviso
print("Material publicado")

input("")