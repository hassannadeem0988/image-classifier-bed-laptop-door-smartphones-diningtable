# 🧠 Image Classifier for Bed, Laptop, Phone, Table, and Door

This is an image classification project that uses a **Convolutional Neural Network (CNN)** to detect and classify images into one of the following 5 categories:

- 🛏️ Bed  
- 💻 Laptop  
- 📱 Smartphone  
- 🍽️ Dining Table  
- 🚪 Door  

The project is built using **TensorFlow**, served via **FastAPI**, containerized with **Docker**, and includes a **Gradio** user interface for easy interaction.

---

## 🗂️ Project Structure

Image Classifier Bed, Laptop, Phone,Table,door/
│
├── api/
│ └── FastApi.py # FastAPI app for prediction
│
├── app/
│ └── gradio_app_interface.py # Gradio interface
│
├── models/
│ └── model_1.keras # Saved trained model
│
├── training/ # Model training code (if needed)
│
├── Dockerfile # Docker instructions
├── requirements.txt # Python dependencies
└── README.md # You're here!

---

## ⚙️ Setup & Installation

### 🔹 Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
fastapi
uvicorn
gradio
tensorflow
pillow
numpy
python-multipart
```
🚀 How to Use
✅ Option 1: 

Gradio Interface

Run the Gradio GUI for quick testing:
```bash
python app/gradio_app_interface.py
```
✅ Option 2: FastAPI Backend

Run the FastAPI server:
```bash
uvicorn api.FastApi:app --host 0.0.0.0 --port 5000
```
🐳 Docker Setup

🔹 Step 1: Build Docker Image
```bash
docker build -t image-classifier-diff-things .
```
🔹 Step 2: Run the Container
```bash
docker run -p 5000:5000 image-classifier-diff-things
```
You can also use Postman for proper prediction testing
```bash
http://0.0.0.0:5000/predict
```
