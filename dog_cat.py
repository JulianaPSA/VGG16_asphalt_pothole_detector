import np as np
from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
from keras.applications.vgg16 import VGG16, decode_predictions

img = image.load_img("VGG16-asphalt_crack_detector/image_cat.jpeg", target_size=(224, 224))
img = np.asarray(img)
plt.imshow(img)
img = np.expand_dims(img, axis=0)
saved_model = VGG16()
output = saved_model.predict(img)
print('Predicted:', decode_predictions(output, top=1)[0])
if output[0][0] > output[0][1]:
    print("dog")
else:
    print('cat')