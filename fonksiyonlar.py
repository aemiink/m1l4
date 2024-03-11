import random
import tensorflow as tf
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np


def yazi_tura():
    para =random.randint(0,2)
    if para == 0:
        return "YAZI"
    else:
        return "TURA"
    
def sifre_olusturucu(sifre_uzunlugu):
    ogeler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    sifre = ""

    for i in range(sifre_uzunlugu):
        sifre += random.choice(ogeler)

    return sifre


def emoji_olusturucu():
     emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
     secilen_emoji = random.choice(emoji)
     return secilen_emoji
 

def get_class(model_path, labels_path, image_path):

    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("keras_Model.h5", compile=False)

    # Load the labels
    class_names = open("labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open("file_url").convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    return "Class:", class_name[2:], "Confidence Score:", confidence_score


