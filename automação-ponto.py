import pyautogui as pgui
from time import sleep
from datetime import datetime, time

current_time = datetime.now().time() # Pega o horario atual e armazena em uma variavel

break_time = time(15, 30, 30) # Define um horario e armazena

while True:
    pgui.hotkey('win','m') # Atalho até a area de trabalho
    sleep(2) # Pausa de 5 segundos


    if current_time == break_time: # Faz a verificação se o horario atual esta igual ao horario do break time
        confirmation = pgui.confirm(title='AUTOMAÇÃO PONTO VIRTUAL', text='DESEJA BATER O PONTO VIRTUAL AGORA?', buttons=['SIM','NÃO', 'CANCELAR']) # Recebe uma confirmação do usuario (sim, não, cancelar)

    if confirmation == 'NÃO': # Caso o usuario escolha a opção 'não' o programa pergunta daqui quanto tempo o usuario deseja realizar a automação e armazena em uma variavel
        temp_minutos = pgui.prompt(title='AUTOMAÇÃO PONTO VIRTUAL', text='DAQUI QUANTO TEMPO DESEJA BATER SEU PONTO? [EM MINUTOS]') 

    elif confirmation == 'CANCELAR':
        break 

    temp_segundos = temp_minutos * 60 # Transforma o tempo de minutos para segundos

    sleep(temp_segundos) # Pausa durante quanto tempo o usuario determinar

    pgui.moveTo(554,35,duration=2) # Move o cursor até o icone do ponto virtual
    sleep(1) # Pausa durante 1 segundo

    pgui.doubleClick() # Realiza a ação de double click para abrir o software
    sleep(10) # Pausa durante 10 segundos

    pgui.moveTo(191,142,duration=2) # Move o cursor até o campo de senha
    sleep(1) # Pausa durante 1 segundo

    pgui.write('MCS931') # Coloca a senha no campo senha
    sleep(1) # Pausa durante 1 segundo

    pgui.moveTo(152,629,duration=2) # Move o cursor até o campo de emoções
    sleep(1) # Pausa durante 1 segundo

    pgui.click() # Clica na emoção desejada
    sleep(1) # Pausa durante 1 segundo

    pgui.moveTo(820,634,duration=2) # Move o mouse até o botão confirmar
    sleep(1) # Pausa durante 1 segundo

    pgui.click() # Clica no botaão confirmar
    sleep(5) # Pausa durante 5 segundos

    pgui.press('Enter') # Pressiona enter para sair do programa
    sleep(2) # Pausa durante 2 segundos

    pgui.alert(title='AUTOMAÇÃO PONTO VIRTUAL', text='PONTO ELETRONICO BATIDO!', button='Ok')
    break