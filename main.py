import numpy as npy
import random
import math
import re
import os
from PIL import Image,ImageDraw
from matplotlib import pyplot as plt
import json

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def imgtofun():
    c=1;
    directorio = os.getcwd();
    folder = directorio + "\\images\\";
    file = os.listdir(folder)[0];
    print(folder);
    imagen = Image.open(folder + file)
    size=(300,300)
    imagen = imagen.resize(size)
    imagen.show()
    imgArray = npy.asarray(imagen);
    print(imgArray.shape)
    data = [];
    valores_rgb = [(r, g, b) for r in range(256) for g in range(256) for b in range(256)]
    grafico = {}
    j = 0
    for fila in imgArray:
        for rgb in fila:
            rgb_tupla = tuple(rgb)
        # Verificar si el valor RGB ya está en el diccionario
            if rgb_tupla not in grafico:
            # Si no está en el diccionario, asignarle un número secuencial único
                grafico[rgb_tupla] = j
                j += 1
    # print(grafico)
    data = Image.fromarray(imgArray);
    j = 0
    for fila in range(imgArray.shape[0]):
        for columna in range(imgArray.shape[1]):
            grafico[j] = imgArray[fila,columna]
            j = j + 1
    print (grafico[20][0])
    plot = []
    for i, rgb in enumerate(valores_rgb):  
        if i != 90000 :
            
            disc = ( grafico[i][0] * 256**2 ) + ( grafico[i][1] * 256**1 ) + ( grafico[i][2] * 256**0 )
            tupla = (i,disc)
            plot.append(tupla)
        else:
            break

    Start_year, End_year = zip(*plot)
    plt.plot(Start_year, End_year)
    plt.show()

    with open("mi_tupla.txt", "w") as archivo:
        for elemento in plot:
            archivo.write(f"{elemento}\n")

    width, height = 300, 300
    image = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(image)
    x = 0
    limit = 0
    print (plot[13000][1])
    for x in range(width):
        for y in range(height):
            b = plot[limit][1] % 256
            g = (plot[limit][1] // 256) % 256
            r = (plot[limit][1] // (256**2)) % 256
            color_rgb = (r, g, b)
            limit = limit + 1
            image.putpixel((y, x), color_rgb)   
    image.save("output.jpg")

imgtofun();