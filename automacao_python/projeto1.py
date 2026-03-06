import os
import time
import pyautogui
import pandas as pd

# Configurações de segurança
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

# 1. Abrir o Firefox e entrar no site
os.system("open -a Firefox 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'")

# 2. Esperar o site carregar (Mac Pro 2012 precisa de tempo)
time.sleep(18)

# 3. Fazer Login
pyautogui.press("tab")
time.sleep(1)
pyautogui.write("pythonimpressionador@gmail.com", interval=0.1)
pyautogui.press("tab")
pyautogui.write("sua senha", interval=0.1) # <--- COLOQUE SUA SENHA AQUI
pyautogui.press("enter")

# Espera o carregamento da página de formulário
time.sleep(12)

# 4. Importar a base de dados
tabela = pd.read_csv("produtos.csv")

# 5. Loop de Cadastro (Agora com a sua coordenada real!)
for linha in tabela.index:
    # CLIQUE NO CAMPO CÓDIGO (Usando a sua coordenada exata: 757, 264)
    pyautogui.click(x=757, y=264, clicks=2)
    time.sleep(1.5) 
    
    # Limpa o campo para garantir que está vazio
    pyautogui.hotkey('command', 'a')
    pyautogui.press('backspace')
    time.sleep(0.5)

    # Digita o Código
    codigo_produto = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo_produto, interval=0.1)
    
    # Navega com TAB para o restante (conforme o que já funcionava)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]), interval=0.1)
    
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]), interval=0.1)
    
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]), interval=0.1)
    
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]), interval=0.1)
    
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]), interval=0.1)
    
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs, interval=0.1)
        
    # Enviar o formulário
    pyautogui.press("tab")
    pyautogui.press("enter") 
    
    # Rolar para o topo para o próximo produto
    pyautogui.scroll(5000)
    time.sleep(3)