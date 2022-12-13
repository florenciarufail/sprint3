import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()



driver.get("https://tienda.centroestant.com.ar/")
time.sleep(2)
acceder=driver.find_element(By.XPATH,"/html/body/div[2]/header/div/div[1]/div/div[3]/ul/li[2]")
acceder.click()
time.sleep(2)
mail=driver.find_element(By.ID,"reg_email")
contraseña=driver.find_element(By.ID,"reg_password")
registrarse=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div[2]/div/div[2]/div/form/p[3]/button")
mail.send_keys("pruebamailflou@HOTMAIL.com")
contraseña.send_keys("A2$@65aaaaaaaaaaa")
time.sleep(2)
registrarse.click()
time.sleep(2)
micuenta=driver.find_element(By.XPATH,"/html/body/div[2]/header/div/div[1]/div/div[3]/ul/li[2]")
micuenta.click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div/div/div/div/div/ul/li[5]").click()
time.sleep(4)
nombre=driver.find_element(By.ID,"account_first_name")
apellido=driver.find_element(By.ID,"account_last_name")
nombre.send_keys("Probando")
apellido.send_keys("probando2")
nombreVisible=driver.find_element(By.ID,"account_display_name") 
nombreVisible.clear()
nombreVisible.send_keys("test1234")
guardar=driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div/div/div/div/div/form/p[5]/button")
guardar.click()
time.sleep(2)
driver.close()