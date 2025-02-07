import pandas as pd
import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write("chrome")
pyautogui.press("enter") 

time.sleep(3)
pyautogui.write("https:www.sauer.pro.br/python/automacao/index.html")
pyautogui.press("enter") 
time.sleep(3)

pyautogui.click(x=1213, y=441)
pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.write("SimplificaPython")

pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

tabela = pd.read_csv("alunos.csv")
time.sleep(3)

for linha in tabela.index:

    pyautogui.click(x=839, y=385)
    nome = tabela.loc[linha,"Nome"]
    pyautogui.write(str(nome))
    pyautogui.press("tab")
    email = tabela.loc[linha,"Email"]
    pyautogui.write(email)
    pyautogui.press("tab")
    endereco = tabela.loc[linha,"Endereco"]
    pyautogui.write(endereco)
    pyautogui.press("tab")
    telefone = tabela.loc[linha,"Telefone"]
    pyautogui.write(telefone)
    pyautogui.press("tab")
    pyautogui.press("enter")
   
    pyautogui.scroll(5000)

