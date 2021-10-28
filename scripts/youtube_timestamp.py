#!/usr/bin/env python3
import time

from glob import glob
path = 'videos/pleno'

for sesion in glob(f'{path}/*.md'):
  youtube_link = None
  if sesion.split('/')[-1] == 'README.md':
    continue

  with open(sesion, 'r') as f:
    for l in f.readlines():
      try:
        if '#' == l.strip()[0]:
          continue
      except:
        pass

      if 'https://youtu.be' in l:
        youtube_link = l.split()[1]
        continue

      token = l.split()
      if len(token):
        token = token[0].split(':')
        if len(token):  
          t = None
          if len(token) == 2:
            t = 60*int(token[0])+int(token[1])
          elif len(token) == 3:
            t = 3600*int(token[0]) + 60*int(token[1]) + int(token[2])
          
          if t:
            print(l, f'{youtube_link}?t={t}')
            #print(t,l)
 
