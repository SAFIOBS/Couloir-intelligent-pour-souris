
#!/usr/bin/env python3
import serial
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
from statistics import mean, stdev

data = deque(maxlen= 1)

ser = serial.Serial('/dev/ttyACM0', 115200)
intervalle_calcul = 1  # 4 secondes

print("⏳ Collecte en cours... Appuyez sur Ctrl+C pour arrêter.")

try:
    debut = time.time()
    dernier_calcul = debut

    while True:
        ligne = ser.readline().decode('utf-8', errors='ignore').strip()

        data.append(ligne)


        numbers = deque(int(x) for x in data[0].split(',') if x.strip() != '')


        print('sum numbers =',sum(numbers))


        if time.time() - dernier_calcul >= intervalle_calcul:
         


            dernier_calcul = time.time()
            ligne = []
 
                       
except KeyboardInterrupt:
    print("\n🛑 Collecte arrêtée par l'utilisateur.")          