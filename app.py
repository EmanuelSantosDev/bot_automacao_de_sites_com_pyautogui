import pyautogui
import webbrowser
from time import sleep

# 1) Navegue até o site https://cursoautomacao.netlify.app/
webbrowser.open('https://cursoautomacao.netlify.app/')
sleep(2)

# 2) Encontre e clique no campo "Digite seu nome" dentro de
# "exemplos Alertas" e digite seu nome
pyautogui.moveTo(694, 195, duration=1)
sleep(1)
pyautogui.scroll(-900)
sleep(1)
nome = pyautogui.locateCenterOnScreen(
    'projetos\\automacao_de_sites_com_pyautogui\\img\\digite_seu_nome.png'
)
pyautogui.click(nome[0], nome[1], duration=1)
pyautogui.click()
pyautogui.typewrite('Emanuel Olivio dos Santos', interval=0.1)
sleep(1)

# 3) Clique em alerta, para gerar a alerta
alerta = pyautogui.locateCenterOnScreen(
    'projetos\\automacao_de_sites_com_pyautogui\\img\\alerta.png'
)
pyautogui.click(alerta[0], alerta[1], duration=1)

# 4) Feche a alerta
pyautogui.move(-215, -235, duration=1.5)
pyautogui.click()
sleep(1)

# 5) Suba a página totalmente para cima
pyautogui.scroll(900)
sleep(1)

# 6) Desça apenas o suficiente para conseguir chegar até a secção
# que contém os arquivos para o quais irá fazer o download e click
# no botão de download para realizar o downlaod dos arquivos excel e pdf
pyautogui.scroll(-2000)
sleep(1)
pyautogui.move(-630, 265, duration=1)
sleep(1)
pyautogui.click()
pyautogui.move(200, 0, duration=1)
pyautogui.click()
sleep(1)

# 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"
pyautogui.alert(
    text='VOCÊ TERMINOU',
    title='Aviso ao Usuário',
    button='Ok'
)
