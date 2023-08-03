from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup



class BotPay:
    def __init__(self, site, cpf, cod_imovel)  :
        self.driver = None
        self.site = site
        self.cpf = cpf
        self.cod_imovel = cod_imovel


    def pay(self):   
        print(self.site, self.cpf, self.cod_imovel)
        driver = webdriver.Chrome()
        driver.get(self.site)

        cpf_cnpj_input = driver.find_element(By.XPATH, "//input[@id='27']")
        cod_imovel_input = driver.find_element(By.XPATH, "//input[@id='26']")
        cpf_cnpj_input.send_keys(self.cpf)
        time.sleep(15)
        cod_imovel_input.send_keys(self.cod_imovel)
        time.sleep(15)
        botao_confirmar = driver.find_element(By.CSS_SELECTOR, "button[class*='btn-solicitacao']") 
        time.sleep(30)
        botao_confirmar.click()
        time.sleep(5)

        table = driver.find_element(By.CLASS_NAME, "lista-solicitacao")

        # Obter o conteúdo HTML da tabela
        table_html = table.get_attribute("outerHTML")

        # Analisar o conteúdo HTML com o BeautifulSoup
        soup = BeautifulSoup(table_html, "html.parser")

        # Encontrar todas as linhas da tabela
        rows = soup.find_all("tr")

        target_comp = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/form/div[1]/div[2]/div/table/tbody/tr[1]/td[1]")
        target_vcto = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/form/div[1]/div[2]/div/table/tbody/tr[1]/td[3]")
        target_valor = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/form/div[1]/div[2]/div/table/tbody/tr[1]/td[4]")
        target_situacao = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/form/div[1]/div[2]/div/table/tbody/tr[1]/td[5]")


        target_values = [target_comp.text, target_vcto.text, target_valor.text, target_situacao.text]

        print("TARGET ALVO =========>", target_values)
        # Iterar pelas linhas para obter os valores das células
        for row in rows:
            # Encontrar todas as células da linha
            cells = row.find_all("td")
            
            # Verificar se a linha contém células (ignorar cabeçalho)
            if len(cells) > 0:
                # Extrair os valores das células e imprimi-los
                competencia = cells[0].text.strip()
                numero_fatura = cells[1].text.strip()
                data_vencimento = cells[2].text.strip()
                valor = cells[3].text.strip()
                situacao = cells[4].text.strip()

                
                if situacao != "Paga":
                    list_values = [competencia, data_vencimento, valor, situacao]
                    print("VALIDACAO 1 OK") 
                    
                    if target_values == list_values:
                        print("=== VALIDACAO 2 OK")
                        print(" Detalhes ==============")
                        print("Competência:", competencia)
                        print("Nº Fatura:", numero_fatura)
                        print("Data de Vencimento:", data_vencimento)
                        print("Valor:", valor)
                        print("Situação:", situacao)                
                        print("Alvo Elemento para clicar", target_situacao)
                        time.sleep(5)
                        target_situacao.click()
                        time.sleep(5)
                        target_visualizar_doc = driver.find_element(By.XPATH, "//button[contains(@class, 'swal-button--baixar')]")
                        time.sleep(5)
                        target_visualizar_doc.click()
                        time.sleep(20)
                        break
            



goRobozinho = BotPay('https://servicos.corsan.com.br/#/solicitacao/1/', '123456789','1234567-8')
goRobozinho.pay()



