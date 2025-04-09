import time

# Modo rápido ou dramático?
pausar = False  # Mude para True se quiser 1 segundo de intervalo entre os números

for num in range(1000, 2004):
    if num % 11 == 5:
        print(num)
        if pausar:
            time.sleep(1)
num = 1000

while num <= 2003:
    if num % 11 == 5:
        print(num)
    num += 1
