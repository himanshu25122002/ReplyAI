# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import torch
import torch.nn.functional as F
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

# --- Load model and tokenizer ---
model_path = "SvaraAI/saved_model"  # path where your trained model is saved
model = DistilBertForSequenceClassification.from_pretrained(model_path)
tokenizer = DistilBertTokenizerFast.from_pretrained(model_path)
model.eval()

# Map ids to labels
id2label = model.config.id2label

# --- Prediction function ---
def predict(text: str):
    inputs = tokenizer(
        text,
        padding="max_length",
        truncation=True,
        max_length=128,
        return_tensors="pt"
    )
    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=1)
        conf, pred_idx = torch.max(probs, dim=1)
        label = id2label[pred_idx.item()]
    return {"label": label, "confidence": float(conf)}

# --- FastAPI app ---
app = FastAPI(title="SvaraAI Reply Classifier")

# Request schema
class PredictRequest(BaseModel):
    text: str

# /predict endpoint
@app.post("/predict")
def predict_reply(request: PredictRequest):
    result = predict(request.text)
    return result

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# --- Run locally ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
