<<<<<<< HEAD
from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = FastAPI()

model = tf.keras.models.load_model("D:\WEBSITE\BioLungNet_Model.h5")

classes = ["Benign","Malignant","Normal"]

def preprocess(img):
    img = img.resize((224,224))
    img = np.array(img)/255.0
    img = np.expand_dims(img, axis=0)
    return img

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    
    img = preprocess(image)

    prediction = model.predict(img)
    pred_class = classes[np.argmax(prediction)]
    confidence = float(np.max(prediction))

    return {
        "prediction": pred_class,
        "confidence": confidence
=======
from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = FastAPI()

model = tf.keras.models.load_model("D:\WEBSITE\BioLungNet_Model.h5")

classes = ["Benign","Malignant","Normal"]

def preprocess(img):
    img = img.resize((224,224))
    img = np.array(img)/255.0
    img = np.expand_dims(img, axis=0)
    return img

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    
    img = preprocess(image)

    prediction = model.predict(img)
    pred_class = classes[np.argmax(prediction)]
    confidence = float(np.max(prediction))

    return {
        "prediction": pred_class,
        "confidence": confidence
>>>>>>> a9b09af6f3f745da79cf34804d80f5c7ec37b81f
    }