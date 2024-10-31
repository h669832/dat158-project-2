import tensorflow as tf
import gradio as gr
from PIL import Image
import numpy as np

# Load the MobileNetV2 model pre-trained on ImageNet
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Preprocess function for images
def preprocess_image(image):
    image = image.resize((224, 224))  # Resize to model's input size
    image = np.array(image) / 255.0   # Normalize to [0,1]
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Predict function
def classify_image(image):
    image = preprocess_image(image)
    preds = model.predict(image)
    decoded_preds = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0]
    label, confidence = decoded_preds[0][1], decoded_preds[0][2]
    return f"Predicted Fruit: {label}, Confidence: {confidence:.2f}"

# Gradio Interface
iface = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),  # Updated syntax
    outputs="text",
    title="Fruit Classifier"
)

if __name__ == "__main__":
    iface.launch()
