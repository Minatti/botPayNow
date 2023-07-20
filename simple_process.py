from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Configurar o caminho para o driver do Chrome
# Certifique-se de baixar a versão correta do ChromeDriver para a versão do Chrome que você está usando
# Você pode encontrar o ChromeDriver em: https://sites.google.com/a/chromium.org/chromedriver/downloads

usuario = 'sadas'
senha = '12364'


def logar():
    driver = webdriver.Chrome()
    driver.get("https://redebrasil-login.vercel.app/")

    usuario_input = driver.find_element(By.ID, "username")
    senha_input = driver.find_element(By.ID, "password")

    usuario_input.send_keys(usuario)
    senha_input.send_keys(senha)

    # Pressionar Enter para enviar o formulário de login
    senha_input.send_keys(Keys.RETURN)


    driver.implicitly_wait(30)

    # Realizar outras ações após o login, se necessário



    # Fechar o navegador
    driver.quit()
logar()


