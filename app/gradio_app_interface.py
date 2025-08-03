import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image
# Load model
MODEL=tf.keras.models.load_model("models/model_1.keras")
# Define classes
class_names = ['bed', 'dining_table', 'door', 'laptop', 'smartphone']
# Preprocess function
def preprocess(image: Image.Image):
    image = image.resize((256, 256))  # adjust to your model input size
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image
# Prediction function
def classify_image(image):
    processed = preprocess(image)
    predictions = MODEL.predict(processed)[0]
    top_class = class_names[np.argmax(predictions)]
    confidence = float(np.max(predictions))
    return f"{top_class} ({confidence*100:.2f}%)"
# Gradio interface
interface=gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type='pil'),
    outputs='text',
    title='Classify Image',
    description='Upload an image of a bed, laptop, smartphone, dining table, or door.'
)
if __name__ == "__main__":
    interface.launch()