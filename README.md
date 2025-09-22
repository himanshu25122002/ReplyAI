# ReplyAI
ML-powered assistant to classify email replies for outbound sales.

# 🚀 ReplyAI – Reply Classification & FastAPI

ReplyAI is an intelligent ML/NLP system that classifies email replies into `positive`, `negative`, or `neutral` categories. It helps sales teams prioritize prospects by automatically identifying interested, uninterested, or neutral responses. The project includes a FastAPI service to serve predictions via a simple API endpoint.

---

## 🌟 Features

- 📧 Classifies email replies as **positive, negative, or neutral**
- 🧠 Uses **DistilBERT transformer model** for contextual understanding
- ⚡ Baseline models like **Logistic Regression** are also included for comparison
- 🌐 Serves predictions via a **FastAPI `/predict` endpoint**
- 📊 Returns **prediction label and confidence score**
- 📝 Includes short reasoning answers for project questions

---

## 🧰 How It Works

1. **Data Preparation**  
   Load and preprocess the dataset (clean text, handle missing values, map labels)

2. **Model Training**  
   Train a baseline model (Logistic Regression) and fine-tune a DistilBERT transformer

3. **Evaluation**  
   Compare accuracy and F1-score of baseline and transformer models

4. **API Deployment**  
   Wrap the trained DistilBERT model into a FastAPI service to serve predictions

---

## 🛠 Setup Instructions

1️⃣ **Open Command Prompt**  

2️⃣ **Navigate to the project folder**  
```bash
cd path\to\ReplyAI
```
3️⃣ **Install requirements**
```bash
pip install -r requirements.txt
```
4️⃣ **Run the FastAPI server**
```bash
uvicorn app:app --reload
```
5️⃣ **Test the API using another Command Prompt**
```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d "{\"text\": \"Looking forward to the demo!\"}"
```

---

## 📊 Model Comparison

**Logistic Regression (baseline):->** Accuracy 0.8427, Weighted F1 0.8404

**DistilBERT (transformer):->** Accuracy 0.8498, Weighted F1 0.8477

***Recommendation: Use DistilBERT in production for higher accuracy and better contextual understanding.***






