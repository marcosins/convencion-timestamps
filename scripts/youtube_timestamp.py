#!/usr/bin/env python3
# ejecutar desde la raiz del proyecto ./scripts/youtube_timestamp.py
import time

from glob import glob
path = 'videos/pleno'

# recorrer los archivos .md dentro de del path
for sesion in sorted(glob(f'{path}/*.md')):
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
      # si la linea tiene este texto, es el link de youtube
      # guardar el link y pasar a la proxima linea
      if 'https://youtu.be' in l:
        youtube_link = l.split()[1]

      # al partir cada linea, borrar el calculo de tiempo
      t = None
      # separar la linea en tokens
      token = l.split()
      # si hay tokens despues del split
      if len(token):
        # separar el primer token ocupando el caracter ':'
        token = token[0].split(':')
        # si hay tokens despues del split
        if len(token):  
          t = None
          # timestamp sin horas
          if len(token) == 2:
            t = 60*int(token[0])+int(token[1])
          # timestamp con horas
          elif len(token) == 3:
            t = 3600*int(token[0]) + 60*int(token[1]) + int(token[2])
          

      # si en la linea obtuve un calculo de tiempo, agrego el link.
      # si no imprimo la misma linea
      if t:
        print(f'{l.strip()}: {youtube_link}?t={t}')
      else:
        print(l.strip())
 
