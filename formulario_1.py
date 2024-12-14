from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
contar = 0

 # Configura el controlador del navegador
driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')  # Asegúrate de tener ChromeDriver en tu PATH o proporciona la ruta completa
 
 # Abre el formulario en el navegador
driver.get('https://forms.gle/bKmAZ4xthzbVgDeE7')  # Reemplaza 'URL_DEL_FORMULARIO' por la URL real del formulario

selectores_xpath = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[25]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[28]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[31]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[34]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[35]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[36]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[37]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[38]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[39]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[40]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[41]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[42]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[43]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[44]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[45]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[46]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[47]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[48]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[49]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[50]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[51]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[52]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[53]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[54]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[55]/div/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[56]/div/div']

print(len(selectores_xpath))

while(True):
 contar += 1
	# Completa las preguntas con respuestas aleatorias
 for pregunta_numero in selectores_xpath:
  pregunta_xpath = pregunta_numero
  opciones_pregunta = driver.find_elements(By.XPATH, pregunta_xpath + '//div[@class="SG0AAe"]/div')
 
  print(len(opciones_pregunta))
    
  opcion_aleatoria = random.choice(opciones_pregunta)
  opcion_aleatoria.click()
 

# Envía el formulario
  enviar_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span')
  enviar_button.click()

# Espera unos segundos para asegurarse de que el formulario se haya enviado correctamente
  time.sleep(5)

  if contar == 2:
    break

  else:
    enviar_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    enviar_button.click()
# Cierra el navegador
