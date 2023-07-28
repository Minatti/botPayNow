import pyautogui, time

# Identificar posição atual do mouse (x, y) a cada intervalo de tempo
# Identificar qual a config de resolução de video do ambiente... (não precisa ser agora)
# Identificar a execucao do pagamento

def wait():
    two_sec = time.sleep(5)

while True:
    
    print("Minha posição atual é: ", pyautogui.position())
    wait()