import numpy as np
import matplotlib.pyplot as plt

def get_first_value_of_pixel_list(l):
 """retourne 1 si la liste du pixel l a la valeur 0 (noir)
  et sinon retourne 0 si la valeur égale à 255 (blanc)"""
  if l[0]==255:
    return 0
  if l[0]==0:
    return 1

path = 'msg.bmp'
im = plt.imread(path, format=1)
n,m,r = im.shape
#processing the image
alpha=[chr(ord('a')+i) for i in range(26)] 
decoder = np.array([alpha+[' '] for j in range(n)])
ch=''
for i in range(n):
  for j in range(m):
    if get_first_value_of_pixel_list(im[i,j]):
      ch+=decoder[i,j]
      break#we know in advance that there's a single black pixel
print(ch)
#c'est bon la dernière version
