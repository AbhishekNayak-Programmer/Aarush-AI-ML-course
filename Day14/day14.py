from PIL import Image 
import numpy as np
import matplotlib.pyplot as plt

image = Image.open('apple.jpg')  

image = image.convert("RGB")

image = image.resize((256, 256)) 

image_array = np.array(image)

image_array = image_array / 255.0

print(image_array.shape)

plt.imshow(image_array)
plt.axis
plt.show()