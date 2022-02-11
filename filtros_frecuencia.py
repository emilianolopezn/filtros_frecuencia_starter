#formato 
#    sample rate, bit depth, channels
#Archivo wav
#Leer wav en scipy
#Escribir wav en scipy
from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.io.wavfile import write

frecuencia_muestreo, muestras = wavfile.read("violin.wav")

print(frecuencia_muestreo)

print("Tipo: " + str(type(muestras)))
print("Dtype (bithdept): " + str(muestras.dtype))
print("shape = " + str(muestras.shape))
canales = 1
if len(muestras.shape) == 1:
    print("# Canales = 1")
else:
    print("# Canales = " + str(muestras.shape[1]))
    canales = muestras.shape[1]
duracion = muestras.shape[0] / frecuencia_muestreo
print("duracion:  " + "{:.2f}".format(duracion) + " segs")

tiempos = np.linspace(0., duracion, muestras.shape[0])

plt.figure()
if canales == 1:
    plt.plot(tiempos, muestras, label="Canal mono")
else:
    plt.plot(tiempos, muestras[:, 0], label="Izquierdo")
    plt.plot(tiempos, muestras[:, 1], label="Derecho")

plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()