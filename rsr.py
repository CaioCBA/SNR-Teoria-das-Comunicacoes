import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

nPower = 0.0001
temp_Rep = 10

Fs, x = wavfile.read("boate_azul.wav")
x = x[:int(temp_Rep*Fs), 1]

n = np.random.normal(np.sqrt(nPower) * temp_Rep*Fs)

xCorrupt = x + n

fig, ax = plt.subplots()

plt.plot(xCorrupt, label="Sinal corrompido")
plt.plot(x, label="Sinal original")
plt.legend()
plt.show()
