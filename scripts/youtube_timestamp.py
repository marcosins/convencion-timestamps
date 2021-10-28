#!/usr/bin/env python3
import time

from glob import glob
path = 'videos/pleno'

# recorrer los archivos .md dentro de del path
for sesion in glob(f'{path}/*.md'):
  # nuevo archivo, aun no hay link de youtube
  youtube_link = None
  # saltar el archivo README.md
  if sesion.split('/')[-1] == 'README.md':
    continue

  # abrir el archivo .md
  with open(sesion, 'r') as f:
    # inicio del archivo
    print(f'\n\n[{sesion}]')
    # recorrer linea a linea
    for l in f.readlines():

      # si la linea parte con un comentario, pasar a la proxima linea
      try:
        if '#' == l.strip()[0]:
          continue
      except:
        pass

      # si la linea tiene este texto, es el link de youtube
      # guardar el link y pasar a la proxima linea
      if 'https://youtu.be' in l:
        youtube_link = l.split()[1]
        continue

      # separar la linea en tokens
      token = l.split()
      # si hay tokens despues del split
      if len(token):
        # separar el primer token ocupando el caracter ':'
        token = token[0].split(':')
        # si hay tokens despues del split
        if len(token):  
          t = None
          # timestamp sin segundos
          if len(token) == 2:
            t = 60*int(token[0])+int(token[1])
          # timestamp con segundos
          elif len(token) == 3:
            t = 3600*int(token[0]) + 60*int(token[1]) + int(token[2])
          
          if t:
            print(f'{l.strip()}: {youtube_link}?t={t}')
 
