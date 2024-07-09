# imports das bibliotecas 
import time 
import pyautogui
import pandas

pyautogui.PAUSE = 4 # pausa entre uma função e outra da biblioteca pyautogui

pyautogui.press("win") # clique no botão windows
pyautogui.write("edge") # digite edge para procurar o navegador
pyautogui.press("enter") # aperte enter para abrir o navegador
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # escreva essa url no navegador 
pyautogui.press("enter") # digite enter

time.sleep(4) # espere 4 segundos

pyautogui.click(x=892, y=455)# clique na posição passada pelo x e y capturada na outra função do arquivo position_ciclk.py
pyautogui.hotkey("ctrl","a") # digite o atalho ctrl + a
pyautogui.write("daniel.teste@gmail.com") #escreva o email do login
pyautogui.press("tab") # aperte tab
pyautogui.write("senha") # escreva a senha do login
pyautogui.click(x=974, y=658) # recupere a posição do mouse com a funçaõ do arquivo position_click.py e clique em logar 

time.sleep(4) # espere 4 segundos para logar 

tabela = pandas.read_csv("produtos.csv") #armazenar na variavel o conteudo que foi lido pela função do pandas 

# for para percorrer o arquivo podutos csv e recuperar dados 
for linha in tabela.index:
    pyautogui.click(x=916, y=307) # clique no campo que foi recuperado pela função do arquivo position_click.py
    
    codigo = str(tabela.loc[linha, "codigo"]) # variavel que vai armazenar o valor recuperado da tabela e transformado em string(texto)
    pyautogui.write(codigo) # escreva o texto recuperado
    pyautogui.press("tab") # aperte tab
    
    marca = str(tabela.loc[linha, "marca"])# variavel que vai armazenar o valor recuperado da tabela e transformado em string(texto)
    pyautogui.write(marca) # escreva o texto recuperado
    pyautogui.press("tab") # aperte tab
    
    tipo = str(tabela.loc[linha, "tipo"])# variavel que vai armazenar o valor recuperado da tabela e transformado em string(texto)
    pyautogui.write(tipo) # escreva o texto recuperado
    pyautogui.press("tab") # aperte tab
    
    categoria = str(tabela.loc[linha, "categoria"])# variavel que vai armazenar o valor recuperado da tabela e transformado em string(texto)
    pyautogui.write(categoria) # escreva o texto recuperado
    pyautogui.press("tab") # aperte tab
    
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])# variavel que vai armazenar o valor recuperado da tabela e transformado em string(texto)
    pyautogui.write(preco_unitario) # escreva o texto recuperado
    pyautogui.press("tab") # aperte tab
    
    custo = str(tabela.loc[linha, "custo"])# variavel que vai armazenar o valor recuperado da tabela e transformado em string(texto)
    pyautogui.write(custo) # escreva o texto recuperado
    pyautogui.press("tab") # aperte tab
    
    obs = str(tabela.loc[linha, "obs"])# variavel que vai armazenar o valor recuperado da tabela e transformado em string(texto)
    if obs != "nan": # se obs for diferente de NaN 
        pyautogui.write(obs) # escreva o texto recuperado
    pyautogui.press("tab") # aperte tab
    
    pyautogui.press("enter") # pressione enter
    pyautogui.scroll(5000) # role 5000 pixels para cima 