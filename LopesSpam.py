from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support import expected_conditions 

listaDeFrases=["Um", "Banho", "Ele", "Vai", "Tomar", "Mafia", "Mafia da Ponte", "Coisas da Vida",
              "Os amigos querem um banho", "Vamos lá lopes", "Bem precisas de um banho", "Ja cheira aqui mal toma banho",
              "Ui que ele e o boss dos banhos", "MAFIA DA PONTE!!!!!!!!!", "PARA A PRÓXIMA É EM COIMBRA!", "VAI VAI VAI VAI CRL!!!!",
              "LOL", "DE VALOR", "ESSA AGUA VAI SABER A MEL"]


driver = webdriver.Firefox()
driver.get("http://m.facebook.com");

emailEle = driver.find_element_by_xpath("//*[@id='m_login_email']")
passEle = driver.find_element_by_xpath("//*[@type='password']")
loginBut = driver.find_element_by_xpath("//input[@type='submit']")

emailEle.send_keys("flaviopenas@gmail.com")
passEle.send_keys("---") #editar isto!
loginBut.click()

driver.get("https://m.facebook.com/photo.php?fbid=3171319862915439&set=a.1027313370649443");
i=0 

while i < 5000:
    WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//textarea[@id='composerInput']"))).click()
    driver.find_element_by_xpath("//textarea[@id='composerInput']").send_keys(random.choice(listaDeFrases))
    driver.find_element_by_xpath("//input[@type='submit']").click()
    driver.get("https://m.facebook.com/photo.php?fbid=3171319862915439&set=a.1027313370649443");
    i+=1
