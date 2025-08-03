from fastapi import FastAPI,File,UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
app = FastAPI()
#Load model
MODEL=tf.keras.models.load_model("models/model_1.keras")
#Class names
CLASS_NAMES=['bed', 'diningtable', 'door', 'laptop', 'smartphone']
@app.get("/")
async def root():
    return {"message": "Hello World"}
def read_file_as_image(data)->np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, axis=0)
    predictions=MODEL.predict(img_batch)
    predicted_class=CLASS_NAMES[np.argmax(predictions[0])]
    confidence=float(np.max(predictions[0]))
    return{
        'Predicted Class': predicted_class,
        "Confidence": round(confidence * 100, 2)
    }
if __name__ == "__main__":
    uvicorn.run(app,host='0.0.0.0',port=5000)

