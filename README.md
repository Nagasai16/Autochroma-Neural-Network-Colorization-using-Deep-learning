# 🎨 AutoChroma: Neural Network Colorization  

This repository contains the source code for a web application that uses deep learning to colorize grayscale images. The goal is to provide an intelligent and user-friendly tool that brings black-and-white photos to life with realistic colors.  

---

## 🎯 Project Goal  

The main objective is to build and deploy a robust image colorization system using advanced neural networks like **CNNs, U-Net, GANs, and DeOldify**. This project serves as a practical application of AI and computer vision for enhancing and restoring images.  

---

## 🗂️ Project Modules  

| # | Module | Status | Description |  
| :--- | :--- | :--- | :--- |  
| 1 | **Model Integration** | ✅ | Pre-trained deep learning models (CNNs, U-Net, GANs) are integrated for accurate image colorization. |  
| 2 | **Image Processing** | ✅ | Uses **OpenCV** to handle grayscale input, preprocess data, and output colorized images. |  
| 3 | **Web Interface** | ✅ | A simple **Flask-powered frontend** for uploading grayscale images and viewing the results. |  
| 4 | **Output Management** | ✅ | Automatically saves input and output images for easy comparison and retrieval. |  

---

## 📂 File Structure  

| File/Folder | Purpose |  
| :--- | :--- |  
| `app.py` | Main Flask app with routes for uploading and colorizing images. |  
| `colorization_backend.py` | Core logic for deep learning model integration and colorization. |  
| `model/` | Contains pre-trained models used for inference. |  
| `static/uploads/` | Stores uploaded grayscale images. |  
| `static/output/` | Stores colorized output images. |  
| `templates/index.html` | Frontend interface for the application. |  
| `README.md` | This file, providing a full project overview. |  

---

## 🚀 How to Run  

1. **Clone the Repository:**  
   ```bash
   git clone <https://github.com/Nagasai16/Autochroma-Neural-Network-Colorization-using-Deep-learning/new/main?filename=README.md>
   cd autochroma
   ```
   
2.**Install Dependencies:**   
    ```bash
    pip install -r requirements.txt
    ```
    
3.**Run the Flask App:**
   ```bash
    python app.py
  
   ```
4.**Access in Browser:**
   Open your browser and go to http://127.0.0.1:5000.

---

### 📚 ***Technologies & Resources***
**Backend:** Python,Flask
**Computer Vision:** OpenCV
**Deep Learning:** TensorFlow,PyTorch
**Models:** CNNs, U-Net, DeOldify, GANs

---

### **📸 Screenshots / Demo**
🔹 Upload Grayscale Image:
🔹 Colorized Output:
(Replace placeholders with actual screenshots from your project run)

---

### **💡Final Thoughts**

> "AutoChroma demonstrates the power of AI in reimagining old memories and enhancing visuals. By combining deep learning and computer vision, this project transforms grayscale images into vivid, lifelike experiences."
  
