from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv
from pygame import mixer 

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

time.sleep(3)
driver.find_element(By.XPATH, '//a[text()=" EXPERIÊNCIAS "]').click()

def run_alarm():
    mixer.init()
    mixer.music.load('loudalarm.mp3')
    mixer.music.set_volume(1)
    mixer.music.play()
    time.sleep(3)

def find_rescues():
    time.sleep(3)
    driver.refresh()
    cards = driver.find_elements(By.TAG_NAME, 'fengstexperience-catalog-card-template-1')
    for card in cards:
        btn1 = card.find_element(By.XPATH, '//button[text()=" RESGATE "]').is_displayed()
        btn2 = card.find_element(By.XPATH, '//button[text()=" RESGATAR "]').is_displayed()
        if(btn1 or btn2):
            run_alarm()
            run_alarm()
            run_alarm()
        else:
            print('Not found')

while True:
    find_rescues()