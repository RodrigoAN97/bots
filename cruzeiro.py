from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://socio5estrelas.com.br/home")

cpf = driver.find_element(By.ID, 'mat-input-0')
cpf.send_keys(os.getenv('CPF'))

pw = driver.find_element(By.ID, 'mat-input-1')
pw.send_keys(os.getenv('PASSWORD'))

driver.find_element(By.XPATH, '//button[text()=" ENTRAR "]').click()

time.sleep(2)
driver.find_element(By.XPATH, '//a[text()=" EXPERIÊNCIAS "]').click()
