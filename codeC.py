import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

img_orig= mpimg.imread("ma_figureverte.jpg")
print(img_orig.shape)
print(img_orig.dtype)

img = np.copy(img_orig)

for x in range(1,img_orig.shape[0]-2):
    for y in range(1,img_orig.shape[1]-2):
        Gx = 0
        Gy = 0
        
        r, v, b =img_orig[x - 1, y - 1]
        Gx += - (r + v + b)
        Gy += - (r + v + b)
        
        r, v, b = img_orig[x-1, y]
        Gx += - 2 * (r + v + b)
        
        r, v, b =img_orig[x - 1, y +1]
        Gx += - (r + v + b)
        Gy +=  (r + v + b)
        
        r, v, b = img_orig[x, y - 1]
        Gy += - 2 * (r + v + b)
        
        r, v, b = img_orig[x, y + 1]
        Gy +=  2 * (r + v + b)
        
        r, v, b =img_orig[x + 1, y - 1]
        Gx +=  (r + v + b)
        Gy += - (r + v + b)
        
        r, v, b = img_orig[x + 1, y ]
        Gx +=  2 * (r + v + b)
        
        r, v, b =img_orig[x + 1, y + 1]
        Gx +=  (r + v + b)
        Gy +=  (r + v + b)
        
        module = math.sqrt((Gx*Gx) + (Gy*Gy))
        
        module = module / 4328*255
        
        module = int(module)
        
        img[x,y] = (module, module, module)
        
        
        
        
        r, v, b = img_orig[x+1, y]
        Gx +=  2 * (r + v + b)
    
sobel = img[:,:,0]
plt.imsave("resultat-sobel.png", img)
plt.figure(1)
plt.imshow(sobel, cmap='gray')
plt.colorbar()
plt.show()
    